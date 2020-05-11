import http.server
import socketserver
import termcolor
from pathlib import Path
import json

PORT = 8080
SERVER = 'rest.ensembl.org'
PARAMS = '?content-type=application/json'
conn = http.client.HTTPConnection(SERVER)

# This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True

# We create a class:
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        req_line = self.requestline.split(" ")
        path_name = req_line[1]
        path_name1 = path_name.split("?")
        path_name2 = path_name1[0]

        contents = Path('Error.html').read_text()
        self.send_response(404)

        try: # To avoid Value and key errors:
            if path_name == "/":
                contents = Path('listspecies.html').read_text()
                contents += Path('karyotype.html').read_text()
                contents += Path('chromosomelength.html').read_text()
                self.send_response(200)

            if path_name2 == "/listspecies":
                contents = """
                       <!DOCTYPE html>
                       <html lang="en">
                       <head>
                           <meta charset="utf-8">
                           <title>LIST SPECIES</title>
                       </head>
                       <body style="background-color: LIGHTSTEELBLUE;">
                             """
                ENDPOINT = "/info/species"
                conn.request("GET", ENDPOINT + PARAMS)
                r1 = conn.getresponse()
                data1 = r1.read().decode("utf-8")
                species_info = json.loads(data1)
                species_dict = species_info["species"]
                limit = path_name1[1].split("=")
                count = 0
                contents += f"<p>The total number of species in ensembl is: {len(species_dict)} </p>"

                if len(limit[1]) >= 1:
                    limit_number = limit[-1]
                    contents += f"<p>The limit you have selected is: {limit_number}</p>"

                    for i in species_dict:
                        if count < int(limit_number):
                            contents += f"<p> -{i['display_name']} </p>"
                            count += 1

                else:
                    for i in species_dict:
                        contents += f"<p> -{i['display_name']} </p>"

                contents += """<a href="http://127.0.0.1:8080/">Main page</a>"""
                contents += "</body></html>"
                self.send_response(200)

            if path_name2 == "/karyotype":
                contents = """
                           <!DOCTYPE html>
                           <html lang="en">
                           <head>
                               <meta charset="utf-8">
                               <title>KARYOTYPE</title>
                           </head>
                           <body style="background-color: LIGHTSTEELBLUE;">
                                 """
                ENDPOINT = "/info/assembly/"
                limit = path_name1[1].split("=")
                conn.request("GET", ENDPOINT + limit[1] + PARAMS)
                r1 = conn.getresponse()
                data1 = r1.read().decode("utf-8")
                karyotype_info = json.loads(data1)
                karyotype_list = karyotype_info["karyotype"]
                contents += f"<h2>The names of the chromosomes of the specie {limit[1]} are:</h2>"

                for i in karyotype_list:
                    contents += f"<p> {i} </p>"
                contents += """<a href="http://127.0.0.1:8080/">Main page</a>"""
                contents += "</body></html>"
                self.send_response(200)

            if path_name2 == "/chromosomelength":
                contents = """
                       <!DOCTYPE html>
                       <html lang="en">
                       <head>
                           <meta charset="utf-8">
                           <title>CHROMOSOME LENGTH</title>
                       </head>
                       <body style="background-color: LIGHTSTEELBLUE;">
                             """
                ENDPOINT = "/info/assembly/"
                limit = path_name1[1].split("=")
                species_name = limit[1].split("&")
                conn.request("GET", ENDPOINT + species_name[0] + PARAMS)
                r1 = conn.getresponse()
                data1 = r1.read().decode("utf-8")
                chromosome_info = json.loads(data1)
                chromosome = chromosome_info["top_level_region"]
                for i in chromosome:
                    if i["name"] == limit[-1]:
                        contents += f"<h2>The length of the chromosome {limit[-1]} of the specie {species_name[0]} is:</h2>"
                        contents += f"<p>{i['length']} </p>"
                    else:
                        contents = Path('Error.html').read_text()
                        self.send_response(404)

                contents += """<a href="http://127.0.0.1:8080/">Main page</a>"""
                contents += "</body></html>"
                self.send_response(200)

        except ValueError:
            contents = Path('Error.html').read_text()
            contents += """<a href="http://127.0.0.1:8080/">Main page</a>"""
            self.send_response(404)
        except KeyError:
            contents = Path('Error.html').read_text()
            contents += """<a href="http://127.0.0.1:8080/">Main page</a>"""

            self.send_response(404)

        # Define the content-type header:
        print(contents)
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(contents))

        return

# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()