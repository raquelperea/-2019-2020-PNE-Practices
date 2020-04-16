from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 7

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "127.0.0.1"
PORT1 = 8080
PORT2 = 8082
c1 = Client(IP, PORT1)
c2 = Client(IP, PORT2)

gene = "FRAT1"
folder = "../Session-04/"
filename = folder + gene + ".txt"
s = Seq("")
s = str(s.read_fasta(filename))

frag = 10
bases = 10
fragments1 = []
fragments2 = []

for i in range(frag):
    print(f"Fragment {i+1}: {s[bases*i:bases*(i+1)]}")
    if (i+1) % 2 == 0:
        fragments1.append(s[bases*i:bases*(i+1)])
    else:
        fragments2.append(s[bases*i:bases*(i+1)])


c1.talk(f"Fragment 1 {fragments1[0]}")
c1.talk(f"Fragment 3 {fragments1[1]}")
c1.talk(f"Fragment 5 {fragments1[2]}")
c1.talk(f"Fragment 7 {fragments1[3]}")
c1.talk(f"Fragment 9 {fragments1[4]}")

c2.talk(f"Fragment 2 {fragments2[0]}")
c2.talk(f"Fragment 4 {fragments2[1]}")
c2.talk(f"Fragment 6 {fragments2[2]}")
c2.talk(f"Fragment 8 {fragments2[3]}")
c2.talk(f"Fragment 10 {fragments2[4]}")


