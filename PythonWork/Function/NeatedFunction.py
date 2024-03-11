def calc():
    x, y = 21, 10

    def add():
        z = x + y
        return z

    def sub():
        z = x - y
        return z
    def mul():
        z=x*y
        return z
    def div():
        z=x//y
        return z
    return add, sub,mul,div

# a will hold reference of add function
# b will hold reference of sub function
a,b,c,d = calc()
print(a())     # it will call add function
print(b())     # it will call sub function
print(c())
print(d())
