from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 6

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "127.0.0.1"
PORT = 8081
c = Client(IP, PORT)


gene = "FRAT1"
folder = "../Session-04/"
filename = folder + gene + ".txt"
s = Seq("")
s = str(s.read_fasta(filename))

frag = 5
bases = 10
fragments = []
for i in range(frag):
    print(f"Fragment {i+1}: {s[bases*i:bases*(i+1)]}")
    fragments.append(s[bases*i:bases*(i+1)])

c.talk(fragments[0])
c.talk(fragments[1])
c.talk(fragments[2])
c.talk(fragments[3])
c.talk(fragments[4])





