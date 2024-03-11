

## Syntax

# Syntax of tarnary operator => value_if_true if condition else value_if_false

is_nice=True

state="nice" if is_nice else "not nice"
print(state)


# Zip() Function

f_name=["Naurangi","Rajesh","Chanchal","Anil","Rahul"]
l_name=["Lal","Kumar","Charu","Yadav","Kumar"]
age=[21,28,21.11,31,20]

print(list(zip(f_name,l_name,age)))

for f_name,l_name,age in zip(f_name,l_name,age):
    print(f"{f_name} {l_name} is {age} year old...")






## unzip() function

data=[('Naurangi', 'Lal', 21),
      ('Rajesh', 'Kumar', 28),
      ('Chanchal', 'Charu', 21.11),
      ('Anil', 'Yadav', 31),
      ('Rahul', 'Kumar', 20)]

f_Name,l_Name ,age=list(zip(*data))
print(f"first name is {f_Name}\nLast name is {l_Name}\nand age is {age}")