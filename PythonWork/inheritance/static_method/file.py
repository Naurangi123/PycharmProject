class A:

    def __init__(self, name):
        self.name = name

    @staticmethod
    def pr_name(f_name, l_name):
        return f_name, l_name


a = A("Naurangi lal")
print(a.pr_name("lal", "naurangi"))
print(A.pr_name("naurangi", "lal"))


# Direct decleared static method

class B:
    x = 12

    def xz(name):
        print("this is static method", name.x)


B.xz = staticmethod(B.xz)
B.xz()
