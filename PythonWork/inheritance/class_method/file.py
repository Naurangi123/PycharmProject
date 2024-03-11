class Person:

    firstName="XYZ"

    def __init__(self,name,l_name):
        self.name=name
        self.l_name=l_name

    @classmethod
    def change_name(cls,new_name):
        cls.firstName=new_name

    def display(self):
        print(self.firstName,self.name,self.l_name)

p=Person("PQR","MNO")
p.display()
Person.change_name("dfg")
p.display()


# Direct decleared Classmethod

class A:
    a=10
    def xyz(name):
        print(" variable is ",name.a)

A.xyz=classmethod(A.xyz)
A.xyz()