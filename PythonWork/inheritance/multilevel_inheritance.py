

#Multilevel Inheritance

class Person:

    def __init__(self, name, emp_id, addr, sal):
        self.name=name
        self.emp_id=emp_id
        self.addr=addr
        self.sal=sal
    def run(self):
        return f"NAme is:{self.name},Addr is :{self.addr}"

class Operson(Person):

    def inherit(self):
        return f"Roll_No is:{self.emp_id},salary is:{self.sal}"

class Data(Person):

    def data(self):
        return f"My name : {self.name},and my roll_no :{self.emp_id},i used to live in : {self.addr},and my salary is :{self.sal}"

class Operation(Person):

    def add(self):
        print(self.name+self.sal)

    def mul(self):
        print(self.sal*self.addr)

    def divide(self):
        print(self.name+self.sal//self.emp_id*self.addr)


p= Person("XYZ", 234, "Duhai", 45000)
print(p.run())
o=Operson("",3456,"",230000)
print(o.inherit())
D=Data("Naurangi lal","Em236","Duhai",34900)
print(D.data())
o=Operation(234,456,678,123)
x=o.add()
y=o.mul()
z=o.divide()
