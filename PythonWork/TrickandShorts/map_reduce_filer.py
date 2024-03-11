

# map (funcion_to_apply,list_of_inputs)

items=[1,3,5,7,2]

squared=[]
for i in items:
    squared.append(i**2)
print(squared)



# Another use of Map() Function

item=[1,3,5,7,6,8,9,2,3]
square=list(map(lambda x:x**2,item))
print(square)


# Map() Function in function using Lambda function

def multiply(x):
    return x*x

def add(x):
    return x+x

funcs=[multiply,add]
for i in range(5):
    value=list(map(lambda x:x(i),funcs))

    print(value)



# Filter()

list_item=range(-7,7)
less_zero=list(filter(lambda x:x<5,list_item))
print(less_zero)



#  Reduce()

pro=1
list=[1,2,3,4,6,8,9]
for num in list:
    pro=pro*num
print(pro)