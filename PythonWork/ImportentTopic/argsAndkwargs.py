

#  In *args function ,we do not need to know how many argyments will passed to your function
#  *args is used to send no-keyworded variable length argument list to the function

#Program

def test(f_arg,*argv):
    print("first normal arg:",f_arg)
    for arg in argv:
        print("another through *argv:",arg)
test("XYZ","Pythion","JAVASCript","test")



#  **kwargs allow to you to pass keyworded variable length of argument to a function..
#  You should use **kwargs if yo u want handle named arguments in a function..

# Program

def greet(**kwargs):
    for key,value in kwargs.items():
        print("{0}={1}".format(key,value))

greet(name="naurangi")