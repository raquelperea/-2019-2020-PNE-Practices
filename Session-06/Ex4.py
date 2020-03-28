import termcolor
class Seq:
    """A class for representing sequence objects"""
    def __init__(self, strbases):
        v = True
        for i in strbases:
            if i != "A" and i != "C" and i != "G" and i != "T":
                v = False

        if v == True:
            self.strbases = strbases

        else:
            strbases = "ERROR"
            self.strbases = strbases
            print("ERROR!!")

    print("New sequence created!")

    def __str__(self):
        return self.strbases

    def len(self):
        return len(self.strbases)


def print_seqs(seq_list, color):
    for i in range(len(seq_list)):
        termcolor.cprint((f"Sequence{i} : (Length:{seq_list[i].len()}) {seq_list[i]}"), color)

def generate_seqs(pattern, number):
    number_list = []
    for i in range(1, number + 1):
        bases = pattern * i
        bases = Seq(bases)
        number_list.append(bases)
    return number_list



seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

termcolor.cprint("List 1:", "blue")
print_seqs((seq_list1), "blue")


termcolor.cprint("List 2:", "green")
print_seqs((seq_list2), "green")