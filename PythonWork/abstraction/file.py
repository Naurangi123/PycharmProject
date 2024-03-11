from abc import ABC, abstractmethod

class Person(ABC):
    @abstractmethod
    def visit(self):
        pass

class Relatives(Person):
    def __init__(self, num, num_float):
        self.num = num
        self.num_float = num_float

    def visit(self):
        print(self.num*self.num_float)

class Homies(Person):
    def visit(self):
        print("Visit Homies")

class Special(Person):
    def visit(self):
        print("Visit Special")

class College(Person):
    def visit(self):
        print("Visit College")

r = Relatives(10, 14)
r.visit()
h = Homies()
h.visit()
s = Special()
s.visit()
c = College()
c.visit()
