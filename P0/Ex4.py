from Seq0 import *

folder = "../Session-04/"
list_genes = ["U5.txt", "FRAT1.txt", "FXN.txt", "ADA.txt", "RNU6_269P.txt"]
bases_list = ["A", "C", "G", "T"]

for e in list_genes:
    print(e)
    for i in bases_list:
        print(i)
        print(seq_count_base(seq_read_fasta(folder + e), i))

