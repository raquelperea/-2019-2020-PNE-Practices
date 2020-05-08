import termcolor

genes = ["FRAT1", "ADA", "FXN", "RNU6_269P", "MIR633", "TTTY4C", "RBMY2YP", "FGFR3", "KDR", "ANK2"]
gene_identifiers = ['ENSG00000165879', 'ENSG00000196839', 'ENSG00000165060', 'ENSG00000212379', 'ENSG00000207552', 'ENSG00000228296', 'ENSG00000227633', 'ENSG00000068078', 'ENSG00000128052', 'ENSG00000145362']

print("Dictionary genes!")
print(f"There are {len(genes)} genes in the dictionary:")

dict_genes = dict(zip(genes, gene_identifiers))


gene_print = ""
for gene, identifier in dict_genes.items():
    gene_print = termcolor.colored(gene, "green")
    print(f"{gene_print}: -> {identifier}")





