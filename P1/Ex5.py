from Seq1 import Seq
# -- Create a Null sequence
s1 = Seq("")

# -- Create a valid sequence
s2 = Seq("ACTGA")

# -- Create an invalid sequence
s3 = Seq("Invalid sequence")

print(f" Sequence 1: (Length : {s1.len()}) {s1} \n A: {s1.count_base('A')}, C: {s1.count_base('C')}, G: {s1.count_base('G')}, T: {s1.count_base('T')}")
print(f" Sequence 2: (Length : {s2.len()}) {s2} \n A: {s2.count_base('A')}, C: {s2.count_base('C')}, G: {s2.count_base('G')}, T: {s2.count_base('T')}")
print(f" Sequence 3: (Length : {s3.len()}) {s3} \n A: {s3.count_base('A')}, C: {s3.count_base('C')}, G: {s3.count_base('G')}, T: {s3.count_base('T')}")



