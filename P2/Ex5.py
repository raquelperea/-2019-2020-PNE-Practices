from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 5

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

gene = "U5"
folder = "../Session-04/"
filename = folder + gene + ".txt"
s = Seq("")

# -- Initialize the null seq with the given file in fasta format
s = str(s.read_fasta(filename))



# -- Parameters of the server to talk to
IP = "127.0.0.1"
PORT = 8081

# -- Create a client object
c = Client(IP, PORT)
c.debug_talk(f"Sending {gene} gene to the server...")
c.debug_talk(s)