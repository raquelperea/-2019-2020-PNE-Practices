from pathlib import Path


def seq_ping():
    print("Ok!")



def seq_read_fasta(filename):
    seq_dna = Path(filename).read_text()
    seq_dna = seq_dna.split("\n")
    seq_dna = seq_dna[1:]
    final_seq = "".join(seq_dna)

    return final_seq

def seq_len(filename):
    return len(filename)


def seq_count_base(seq, base):
    count = 0
    for i in seq:
        if i == base:
            count += 1
    return count


def seq_count(seq):
    bases_list = ["A", "C", "G", "T"]
    count_list = []
    for e in bases_list:
        count_list.append(seq_count_base(seq, e))
    dict_seq = dict(zip(bases_list, count_list ))
    return dict_seq

def seq_reverse(seq):
    reverse_seq = ""
    for e in seq[::-1]:
        reverse_seq += e
    return reverse_seq

def seq_complement(seq):
    complement_seq = ""
    for e in seq:
        if e == "A":
            complement_seq += "T"
        elif e == "T":
            complement_seq += "A"
        elif e == "C":
            complement_seq += "G"
        elif e == "G":
            complement_seq += "C"
    return complement_seq






