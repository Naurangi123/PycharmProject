# single Inheritance

class Data:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

class Operation(Data):

    def opertor(self):
        print(self.a+self.b*self.c//self.d)

o = Operation(12, 34, 56, 78)
o.opertor()
