class A:

    def __init__(self,a,b,c,d,x,p,q,r,m):
        self.a=a
        self.b=b
        self.c = c
        self.d = d
        self.x = x
        self.p = p
        self.q = q
        self.r = r
        self.m = m

class B:
    def power(self):
        return self.a**self.b
class C(A,B):

    def cubic(self):
        return (self.c**self.d)*self.x

    def parenthesis(self):
        return (self.p*(self.q-(self.r*self.m)))


c=C(10,20,12,34,56,78,34,56,10)
print(c.power())
print(c.cubic())
print(c.parenthesis())
