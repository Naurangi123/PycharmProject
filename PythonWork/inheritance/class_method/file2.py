class Student:
    name = "Naurangi Lal"
    def __init__(self, f_name, l_name):
        self.f_name = f_name
        self.l_name = l_name
    def show(self):
        return self.f_name ,self.l_name
    @classmethod
    def change_name(cls,new_name):
        print(Student.name)
        cls.name=new_name

s = Student("XYZ", "ITR")
print(s.show())
Student.change_name("Naurangi")
