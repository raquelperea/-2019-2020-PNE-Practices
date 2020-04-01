from Seq1 import Seq

folder = "../Session-04/"
list_genes = ["U5.txt", "FRAT1.txt", "FXN.txt", "ADA.txt", "RNU6_269P.txt"]
bases_list = ["A", "C", "G", "T"]
s = Seq("")

for e in list_genes:
    s = s.read_fasta(folder + e)
    max_base = ""
    count_values = 0
    for key, value in s.count().items():
        while value > count_values:
            count_values = value
            max_base = key

    print("Gene", e,":", "The most repeated base is:", max_base)
