class Seq:
    """A class for representing sequence objects"""
    def __init__(self, strbases):
        self.strbases = strbases
        print("New sequence created!")


    def __str__(self):
        return self.strbases

    def __len__(self):
        return len(self.strbases)

class Gene(Seq):
    """This class is derived from the Seq Class
          All the objects of class Gene will inheritate
          the methods from the Seq class
       """

    def __init__(self, strbases, name=""):
        # -- Call first the Seq initilizer and then the
        # -- Gene init method
        super().__init__(strbases)
        self.name = name
        print("New gene created")

    def __str__(self):
        """Print the Gene name along with the sequence"""
        return self.name + "-" + self.strbases
    pass


# --- Main program
s1 = Seq("AGTACACTGGT")
g = Gene("CGTAAC", "FRAT1")

# -- Printing the objects
print(f"Sequence 1: {s1}")
print(f"Gene: {g}")

print(f"The length of the sequence 1 is {s1.len()}")
print(f"The length of the sequence 2 is {g.len()}")


print("Testing objects...")

