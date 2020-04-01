from Seq1 import Seq

# -- Create a Null sequence
s = Seq("")

# -- Initialize the null seq with the given file in fasta format
s.read_fasta("../Session-04/U5.txt")

#print(f" Sequence: (Length : {s.len()}) {s} \n Bases: {s.count()} \n Rev: {s.reverse()} \n Comp: {s.complement()}")
print(f" Sequence: (Length : {s.len()}) {s} \n Bases: {s.count()} \n Rev: {s.reverse()} \n Comp: {s.complement()}")
