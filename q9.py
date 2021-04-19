class myclass:
    """
    def __init__(self, name):
        self.name = name
    """

    def get_string(self, myname):
        self.name = myname

    def print_sring(self):
        s = self.name.upper()
        print(s)


p1 = myclass()
p1.get_string(input("enter your name "))
p1.print_sring()
