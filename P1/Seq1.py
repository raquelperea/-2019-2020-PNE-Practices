from pathlib import Path
class Seq:
    """A class for representing sequence objects"""
    def __init__(self, strbases):
        if len(strbases) == 0:
            print("NULL Seq Created")
            self.strbases = "NULL"
        else:
            for i in strbases:
                if i not in ["A", "C", "G", "T"]:
                    print("INVALID seq")
                    self.strbases = "ERROR"
                    return
            self.strbases = strbases
            print("New sequence created!")



    def __str__(self):
        return self.strbases

    def len(self):
        for i in self.strbases:
            if i not in ["A", "C", "G", "T"]:
                return 0
        return len(self.strbases)

    def count_base(self, base):
        count = 0
        for i in self.strbases:
            if i == base:
                count += 1
        return count


    def count(self):
        bases_list = ["A", "C", "G", "T"]
        value_list = []
        for i in bases_list:
            value_list.append(self.count_base(i))
        return dict(zip(bases_list, value_list))



    def reverse(self):
        reverse_seq = ""
        if self.strbases == "NULL":
            return self.strbases
        else:
            for i in self.strbases[::-1]:
                if i not in ["A", "C", "G", "T"]:
                    reverse_seq = "ERROR"
                    return reverse_seq

                else:
                    reverse_seq += i
        return reverse_seq


    def complement(self):
        comp_seq = ""
        if self.strbases == "NULL":
            return self.strbases
        else:
            for i in self.strbases:
                if i not in ["A", "C", "G", "T"]:
                    comp_seq = "ERROR"
                    return comp_seq

                else:
                    if i == "A":
                        comp_seq += "T"
                    elif i == "T":
                        comp_seq += "A"
                    elif i == "C":
                        comp_seq += "G"
                    else:
                        comp_seq += "C"
            return comp_seq


    def read_fasta(self, filename):
        self.strbases = Path(filename).read_text()
        self.strbases = self.strbases.split("\n")
        self.strbases = self.strbases[1:]
        #self.strbases = str(self.strbases)
        self.strbases = "".join(self.strbases)
        return self






