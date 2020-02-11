#Write a program that opens the dna.txt file and calculates the total number of bases,
# and the number of the different bases


f = open("dna.txt", 'r')
file2 = f.read()
seq = file2.strip('\n')
f.close()

count = 0
countA = 0
countC = 0
countT = 0
countG = 0

for i in seq:
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