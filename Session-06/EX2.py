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


def print_seqs(seq_list):
    for i in range(len(seq_list)):
        print(i, seq_list[i].len(), seq_list[i])


seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]
print_seqs(seq_list)

