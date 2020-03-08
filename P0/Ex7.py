from Seq0 import *

seq_20 = seq_read_fasta("../Session-04/U5.txt")[:20]
print(seq_20)
print(seq_complement(seq_20))