from Seq0 import *
folder = "../Session-04/"
list_genes = ["U5.txt", "FRAT1.txt", "FXN.txt", "ADA.txt", "RNU6_269P.txt"]

for i in list_genes:
    print(i)
    i = seq_read_fasta(folder + i)
    print(seq_count(i))