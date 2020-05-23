import http.server
import socketserver
import termcolor
from pathlib import Path
import json
from Seq1 import *

PORT = 8080
SERVER = 'rest.ensembl.org'
PARAMS = '?content-type=application/json'
conn = http.client.HTTPConnection(SERVER)

# This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True

# We create a class:
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
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
                contents += Path('geneSeq.html').read_text()
                contents += Path('geneInfo.html').read_text()
                contents += Path('geneCalc.html').read_text()
                contents += Path('geneList.html').read_text()
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
                           <body style="background-color: LIGHTBLUE;">
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
                       <body style="background-color: LIGHTBLUE;">
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
                contents += """<a href="http://127.0.0.1:8080/">Main page</a>"""
                contents += "</body></html>"
                self.send_response(200)

            if path_name2 == "/geneSeq":
                contents = """
                       <!DOCTYPE html>
                       <html lang="en">
                       <head>
                           <meta charset="utf-8">
                           <title>GENE SEQUENCE</title>
                       </head>
                       <body style="background-color: LIGHTBLUE;">
                             """
                ENDPOINT1 = "/xrefs/symbol/homo_sapiens/"
                genes = path_name1[1].split("=")
                genename = genes[1]
                PARAMS1 = genename + PARAMS
                conn.request("GET", ENDPOINT1 + PARAMS1)
                r1 = conn.getresponse()
                data1 = r1.read().decode("utf-8")
                id_dict = json.loads(data1)
                id_dict = id_dict[0]
                id_number = id_dict["id"]

                ENDPOINT2 = "/sequence/id/"
                PARAMS2 = id_number + PARAMS
                conn.request("GET", ENDPOINT2 + PARAMS2)
                r2 = conn.getresponse()
                data2 = r2.read().decode("utf-8")
                seq_dict = json.loads(data2)
                seq_complete = seq_dict['seq']
                contents += f"<h2>The sequence of  {genename} is:</h2>"
                contents += f"<textarea readonly rows = 20 cols = 80>{seq_complete} </textarea>"

                contents += """<a href="http://127.0.0.1:8080/">Main page</a>"""
                contents += "</body></html>"
                self.send_response(200)

            if path_name2 == "/geneInfo":
                contents = """
                       <!DOCTYPE html>
                       <html lang="en">
                       <head>
                           <meta charset="utf-8">
                           <title>GENE INFO</title>
                       </head>
                       <body style="background-color: LIGHTSTEELBLUE;">
                             """
                ENDPOINT1 = "/xrefs/symbol/homo_sapiens/"
                genes = path_name1[1].split("=")
                genename = genes[1]
                PARAMS1 = genename + PARAMS
                conn.request("GET", ENDPOINT1 + PARAMS1)
                r1 = conn.getresponse()
                data1 = r1.read().decode("utf-8")
                id_dict = json.loads(data1)
                id_dict = id_dict[0]
                id_number = id_dict["id"]

                ENDPOINT2 = "/sequence/id/"
                PARAMS2 = id_number + PARAMS
                conn.request("GET", ENDPOINT2 + PARAMS2)
                r2 = conn.getresponse()
                data2 = r2.read().decode("utf-8")
                seq_dict = json.loads(data2)
                seq_complete = seq_dict['seq']

                ENDPOINT3 = '/lookup/id/'
                PARAMS3 = id_number + PARAMS
                conn.request("GET", ENDPOINT3 + PARAMS3)
                r3 = conn.getresponse()
                data3 = r3.read().decode("utf-8")
                gene_dict = json.loads(data3)
                seq_complete = Seq(seq_complete)
                contents += f"<h2>The information of {genename} is:</h2>"
                contents += f"<p>The start is: {gene_dict['start']}</p>"
                contents += f"<p>The end is: {gene_dict['end']} </p>"
                contents += f"<p>The length is: {seq_complete.len()} </p>"
                contents += f"<p>The id is: {id_number}</p>"
                contents += f"<p>The chromosome is: {gene_dict['seq_region_name']} </p>"
                contents += """<a href="http://127.0.0.1:8080/">Main page</a>"""
                contents += "</body></html>"
                self.send_response(200)

            if path_name2 == "/geneCalc":
                bases = ["A", "C", "G", "T"]
                contents = """
                       <!DOCTYPE html>
                       <html lang="en">
                       <head>
                           <meta charset="utf-8">
                           <title>GENE CALCULATIONS</title>
                       </head>
                       <body style="background-color: LIGHTSTEELBLUE;">
                             """
                ENDPOINT1 = "/xrefs/symbol/homo_sapiens/"
                genes = path_name1[1].split("=")
                genename = genes[1]
                PARAMS1 = genename + PARAMS
                conn.request("GET", ENDPOINT1 + PARAMS1)
                r1 = conn.getresponse()
                data1 = r1.read().decode("utf-8")
                id_dict = json.loads(data1)
                id_dict = id_dict[0]
                id_number = id_dict["id"]

                ENDPOINT2 = "/sequence/id/"
                PARAMS2 = id_number + PARAMS
                conn.request("GET", ENDPOINT2 + PARAMS2)
                r2 = conn.getresponse()
                data2 = r2.read().decode("utf-8")
                seq_dict = json.loads(data2)
                seq_complete = seq_dict['seq']
                seq_complete = Seq(seq_complete)
                contents += f"<h2>The calculations of {genename} is:</h2>"
                contents += f"<p>The length is: {seq_complete.len()} </p>"

                for i in bases:
                    contents += f"<p>{i}: {seq_complete.count_base(i)} ({round((seq_complete.count_base(i) / seq_complete.len()) * 100, 2)}%)</p>"
                contents += """<a href="http://127.0.0.1:8080/">Main page</a>"""
                contents += "</body></html>"
                self.send_response(200)

            if path_name2 == "/geneList":
                contents = """
                          <!DOCTYPE html>
                          <html lang="en">
                          <head>
                              <meta charset="utf-8">
                              <title>GENE LIST</title>
                          </head>
                          <body style="background-color: LIGHTSTEELBLUE;">
                                """
                ENDPOINT = '/overlap/region/human/'
                arguments = path_name1[-1].split("&")
                list_arguments = []
                for argument in arguments:
                    list_arguments.append(argument.split("=")[1])

                PARAMS_LIST = list_arguments[0] + ':' + list_arguments[1] + '-' + list_arguments[2] + '?feature=gene;content-type=application/json'
                conn.request("GET", ENDPOINT + PARAMS_LIST)
                r1 = conn.getresponse()
                data1 = r1.read().decode("utf-8")
                chromo_list = json.loads(data1)
                contents += f"<h2>The list of genes in the chromosome {list_arguments[0]} between {list_arguments[1]} and {list_arguments[-1]} is:</h2>"
                for i in chromo_list:
                    gene_name = i["external_name"]
                    contents += f"<p> {gene_name} </p>"
                contents += """<a href="http://127.0.0.1:8080/">Main page</a>"""
                contents += "</body></html>"
                self.send_response(200)

        except ValueError:
            contents = Path('Error.html').read_text()
            contents += f"<p>This is a ValueError type </p>"
            contents += """<a href="http://127.0.0.1:8080/">Main page</a>"""
            self.send_response(404)
        except KeyError:
            contents = Path('Error.html').read_text()
            contents += f"<p>This is a KeyError type </p>"
            contents += """<a href="http://127.0.0.1:8080/">Main page</a>"""
            self.send_response(404)
        except IndexError:
            contents = Path('Error.html').read_text()
            contents += f"<p>This is an IndexError type </p>"
            contents += """<a href="http://127.0.0.1:8080/">Main page</a>"""
            self.send_response(404)
        except TypeError:
            contents = Path('Error.html').read_text()
            contents += f"<p>This is a TypeError type </p>"
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

Handler = TestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()