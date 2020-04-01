from Seq1 import Seq
# -- Create a Null sequence
s1 = Seq("")

# -- Create a valid sequence
s2 = Seq("ACTGA")

# -- Create an invalid sequence
s3 = Seq("Invalid sequence")

print(f" Sequence 1: (Length : {s1.len()}) {s1} \n {s1.count()}")
print(f" Sequence 2: (Length : {s2.len()}) {s2} \n {s2.count()}")
print(f" Sequence 3: (Length : {s3.len()}) {s3} \n {s3.count()}")
