from pathlib import Path


def seq_ping():
    print("Ok!")



def seq_read_fasta(filename):
    seq_dna = Path(filename).read_text()
    seq_dna.split("\n")

    return seq_dna


print(seq_read_fasta("../Session-04/U5.txt"))

