from Seq1 import Seq
# -- Create a Null sequence
s1 = Seq("")

# -- Create a valid sequence
s2 = Seq("ACTGA")

# -- Create an invalid sequence
s3 = Seq("Invalid sequence")

print(f" Sequence 1: (Length : {s1.len()}) {s1} \n Bases: {s1.count()} \n Rev: {s1.reverse()} \n Comp: {s1.complement()}")
print(f" Sequence 2: (Length : {s2.len()}) {s2} \n Bases: {s2.count()} \n Rev: {s2.reverse()} \n Comp: {s2.complement()}")
print(f" Sequence 3: (Length : {s3.len()}) {s3} \n Bases: {s3.count()} \n Rev: {s3.reverse()} \n Comp: {s3.complement()}")
