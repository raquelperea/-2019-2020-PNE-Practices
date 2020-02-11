#Create a program for counting the number of bases presented in a DNA sequence.
# The user introduces a sequence of letter representing the DNA chain. For example: CATGTAGACTAG.
# Our program should calculate the total length, and the number of bases that compound the sequence.


dna_seq = input("Introduce the sequence:")

count = 0
countA = 0
countC = 0
countT = 0
countG = 0

for i in dna_seq:
    count += 1
    if i == "A":
        countA += 1
    elif i == "C":
        countC += 1
    elif i == "T":
        countT += 1
    else:
        countG += 1

print("Total length: ", count)
print("A: ", countA)
print("C: ", countC)
print("T: ", countT)
print("G: ", countG)

