def add(*args):
    for n in args:
        print(n)
add(3,4,5,6,7,8,90)


def add(*args):
    sum=0
    for n in args:
        sum+=n
    return sum
print(add(3,4,5,7,9,8,1,3,5))



def calculate(n, **kwargs):

    print(kwargs)
    #for i in range():
    n+=kwargs["add"]
    n*=kwargs["multiply"]
    print(n)

calculate(2,add=2,multiply=7)


class Car:
    def __init__(self,**kw):
        self.make=kw.get("make")
        self.model=kw.get("model")
        self.model = kw.get("color")
        self.model = kw.get("seats")

my_car=Car(make="NIsaan",model="GTR")
print(my_car.make,my_car.model)