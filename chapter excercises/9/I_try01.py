class SomeOne:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def addition(self, third):
        self.third = third
        print(f"third is {self.third}")

    def addagin(self):
        print(f"first: {self.first}")
        print(f"second: {self.second}")


class ThisOne(SomeOne):
    def __init__(self, first, second):
        super().__init__(first, second)

    def ghhhh(self):
        print(f"we have {self.first}, {self.second}")


info = SomeOne("thh", "afa")
info2 = ThisOne("afawfw", "Asdfawg")

print(info.addagin())
print(info2.ghhhh())

