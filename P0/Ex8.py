from Seq0 import *

folder = "../Session-04/"
list_genes = ["U5.txt", "FRAT1.txt", "FXN.txt", "ADA.txt", "RNU6_269P.txt"]
bases_list = ["A", "C", "G", "T"]


for e in list_genes:
    print(e)
    max_base = ""
    count_values = 0
    for key, value in seq_count(seq_read_fasta(folder + e)).items():
        while value > count_values:
            count_values = value
            max_base = key

    print("The most repeated base is:", max_base)



