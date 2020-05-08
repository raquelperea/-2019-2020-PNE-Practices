import http.client
import json
import termcolor as termcolor
from Seq1 import Seq

genes = ["FRAT1", "ADA", "FXN", "RNU6_269P", "MIR633", "TTTY4C", "RBMY2YP", "FGFR3", "KDR", "ANK2"]
gene_identifiers = ['ENSG00000165879', 'ENSG00000196839', 'ENSG00000165060', 'ENSG00000212379', 'ENSG00000207552', 'ENSG00000228296', 'ENSG00000227633', 'ENSG00000068078', 'ENSG00000128052', 'ENSG00000145362']
dict_genes = dict(zip(genes, gene_identifiers))

for gene in genes:

    SERVER = 'rest.ensembl.org'
    ENDPOINT = '/sequence/id/'
    PARAMS = dict_genes[gene] + '?content-type=application/json'
    URL = SERVER + ENDPOINT + PARAMS
    bases = ["A", "C", "G", "T"]

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
    print(f"{gene_color}: {gene}")

    description_colored = termcolor.colored("Description", "green")
    print(f"{description_colored}: {gene_info['desc']}")

    seq = Seq(gene_info['seq'])

    length_colored = termcolor.colored("Total length:", "green")
    print(f"{length_colored}: {seq.len()}")

    for i in bases:
        i_colored = termcolor.colored(i, 'blue')
        print(f" {i_colored}: {seq.count_base(i)} {round((seq.count_base(i) / seq.len()) * 100, 2)}%")

    freq_base = termcolor.colored("Most frequence base:", "green")

    max_base = ""
    count_values = 0
    for key, value in seq.count().items():
        while value > count_values:
            count_values = value
            max_base = key

    print(f"{freq_base}", max_base)