import http.client
import json
import termcolor as termcolor

SERVER = 'rest.ensembl.org'
ENDPOINT = '/sequence/id/'
PARAMS ='ENSG00000207552?content-type=application/json'
URL = SERVER + ENDPOINT + PARAMS
IDENTIFIER = "ENSG00000207552"


genes = ["FRAT1", "ADA", "FXN", "RNU6_269P", "MIR633", "TTTY4C", "RBMY2YP", "FGFR3", "KDR", "ANK2"]
gene_identifiers = ['ENSG00000165879', 'ENSG00000196839', 'ENSG00000165060', 'ENSG00000212379', 'ENSG00000207552', 'ENSG00000228296', 'ENSG00000227633', 'ENSG00000068078', 'ENSG00000128052', 'ENSG00000145362']
dict_genes = dict(zip(genes, gene_identifiers))

print()
print(f"Server {SERVER}")
print(f"URL: {URL}")

# Connect with the server
conn = http.client.HTTPConnection(SERVER)

try:
    conn.request("GET", ENDPOINT + PARAMS)
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

r1 = conn.getresponse()

# -- Print the status line
print(f"Response received!: {r1.status} {r1.reason}\n")

# -- Read the response's body
data1 = r1.read().decode("utf-8")

# -- Create a variable with the data,
# -- form the JSON received
gene_info = json.loads(data1)

gene_color = termcolor.colored("Gene", "green")
for gene, identifier in dict_genes.items():
    if identifier == IDENTIFIER:
        print(f"{gene_color}: {gene}")

description_colored = termcolor.colored("Description", "green")

print(f"{description_colored}: {gene_info['desc']}")

bases_colored = termcolor.colored("Bases", "green")
print(f"{bases_colored}: {gene_info['seq']}")


