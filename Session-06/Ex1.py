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


s1 = Seq("ACCTGC")
s2 = Seq("Hello? Am I a valid sequence?")
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")