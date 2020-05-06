import http.server
import socketserver
import termcolor
from Seq1 import *
from pathlib import Path

# Define the Server's port
PORT = 8080
gene_list = ["AAAAGTAGTAGTACATCTCCGTAGACGTGACGTGGGCA", "TGACGAGATAAGCAGTACGATAGCGATACGTGCAGTGC", "GGGGCTCGCCGACAGATAGACAGTCGATAGCAGATAGA", "CCCTGGAGATAGACGTAGCTGACGTCGACGTCGATCGA", "GAGATAGACGATGCGTGCGGTAGCGCAGTCGTAGAGAA" ]

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        req_line = self.requestline.split(" ")
        path_name = req_line[1]
        path_name1 = path_name.split("?")
        path_name2 = path_name1[0]


        contents = Path('Error.html').read_text()
        self.send_response(404)

        if path_name2 == "/":
            contents = Path('form-1.html').read_text()
            contents += Path('form-2.html').read_text()
            contents += Path('form-3.html').read_text()
            contents += Path('form-4.html').read_text()

        else:
            option = path_name1[1].split("=")

            if path_name2 == "/ping":
               contents =  """
                    <!DOCTYPE html>
                    <html lang="en">
                    <head>
                        <meta charset="utf-8">
                        <title>RESULT</title>
                    </head>
                    <body>
                    <h2>PING OK!</h2>
                    <p>The SEQ2 server is running...</p>
                    <a href="http://127.0.0.1:8080/">Main page</a>
                     """
               contents += "</body></html>"
               self.send_response(200)

            elif path_name2 == "/sequence":
                contents = """
                       <!DOCTYPE html>
                       <html lang="en">
                       <head>
                           <meta charset="utf-8">
                           <title>RESULT</title>
                       </head>
                       <body>
                        """
                for i in range(len(gene_list)):
                    if i == int(option[1]):
                        contents += f"<h2> Sequence number {i} </h2>"
                        contents += f"<p> {gene_list[i]} </p>"
                        contents += """<a href="http://127.0.0.1:8080/">Main page</a>"""
                        contents += "</body></html>"
                        self.send_response(200)

            elif path_name2 == "/gene":
                folder = "../Session-04/"
                contents = """
                       <!DOCTYPE html>
                       <html lang="en">
                       <head>
                           <meta charset="utf-8">
                           <title>RESULT</title>
                       </head>
                       <body>
                        """
                seq = Seq("")
                seq = str(seq.read_fasta(folder + option[1] + ".txt"))
                contents += f"<h2> Gene: {option[1]} </h2>"
                contents += f"<textarea readonly rows = 20 cols = 80>{seq}</textarea>"
                contents += "<br>"
                contents += """<a href="http://127.0.0.1:8080/">Main page</a>"""
                contents += "</body></html>"
                self.send_response(200)

            elif path_name2 == "/operation":
                bases = ["A", "C", "G", "T"]
                sequence = option[1].split("&")
                seq = Seq(sequence[0])
                contents = """
                       <!DOCTYPE html>
                       <html lang="en">
                       <head>
                           <meta charset="utf-8">
                           <title>RESULT</title>
                       </head>
                       <body>
                        """
                contents += f"<h2> Sequence </h2>"
                contents += f"<p> {sequence[0]} </p>"
                contents += f"<h2> Operation </h2>"

                if option[-1] == "INFO":
                    contents += "<p> info </p>"
                    contents += f"<h2> Result </h2>"
                    contents += f"<p> Total length{seq.len()} </p>"

                    for i in bases:
                        contents += f"<p>{i} : {seq.count_base(i)} ({round(seq.count_base(i) * (100 / seq.len()), 2)}%)</p>"
                    contents += """<a href="http://127.0.0.1:8080/">Main page</a>"""
                    contents += "</body></html>"
                    self.send_response(200)

                if option[-1] == "COMP":
                    contents += "<p> comp </p>"
                    contents += f"<h2> Result </h2>"
                    contents += f"<p> {seq.complement()}"
                    contents += "<br>"
                    contents += """<a href="http://127.0.0.1:8080/">Main page</a>"""
                    contents += "</body></html>"
                    self.send_response(200)

                if option[-1] == "REV":
                    contents += "<p> rev </p>"
                    contents += f"<h2> Result </h2>"
                    contents += f"<p> {seq.reverse()}"
                    contents += "<br>"
                    contents += """<a href="http://127.0.0.1:8080/">Main page</a>"""
                    contents += "</body></html>"
                    self.send_response(200)


        # Define the content-type header:
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