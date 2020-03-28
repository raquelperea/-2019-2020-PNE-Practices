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
        






class Gene(Seq):
    pass


