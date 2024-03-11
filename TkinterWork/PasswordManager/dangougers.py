try:
    import string
except:
    print("please install strings lib with command <sudo pip3 install ")
try:
    import random
except:
    print("please install random lib with command <sudo pip3 install random>1")
try:
    import os
except:
    print("pleas install the os lib with command <sudo pip install os>")


def switch_case_no():
    dict_no = {"no": 0, "n": 0, "No": 0, "N": 0, "NO": 0}
    return dict_no


def switch_case_yes():
    dict_yes = {"yes": 1, "y": 1, "Yes": 1, "Y": 1, "YES": 1}
    return dict_yes


int_list = str(["1"+"2"+"3"+"4"+"5"+"6"+"7"+"8"+"9"+"0"])
sym_list = str(["~"+"!"+"@"+"#"+"$"+"%"+"^"+"&"+"*"+"("+")"+"_"+"+"+"|"+"?"+">"+"<"])
i = int_list
s = sym_list
l = string.ascii_lowercase
u = string.ascii_uppercase
list_int_1 = tuple(f"{i}")
list_sym_1 = tuple(f"{s}")
list_str_l_1 = tuple(f"{l}")
list_str_u_1 = tuple(f"{u}")


def checker(this_list):  # function to check and generate password list
    x = False  # loop broker
    while not x:  # start of the loop
        password = "".join(random.sample(this_list, k=len1))
        print(f">>>>>>!!!{password}!!!<<<<<<<\r", end="")
        if password == entry:
            print(f"the password is : " "\n""*****>>>>>>>>{password}<<<<<<<<*****\n created by PeterHattson")
            x = True
            try:
                os.system("beep -f 759 -l 400")
            except Exception:
                print("the system beep has not founded !!!!")
            break  # end of the while loop


entry = input("inter your pass >>>>  ")  # you can change this line with any login page that you want
ask_user_int = input("you password has an integer ??? ")
if ask_user_int in switch_case_yes():
    print(">>>>ckuF Your password contain with integers <<<<")
elif ask_user_int in switch_case_no():
    print(">>>>ckuF Your password will not contain with integers <<<<")
else:
    print("please just use yes/y or no/n ")
ask_user_sym = input("your password has a special symbols ??? ")
if ask_user_sym in switch_case_yes():
    print(">>>>ckuF Your password contain with symbols <<<<")
elif ask_user_sym in switch_case_no():
    print(">>>>ckuF Your password will not contain with symbols <<<<")
else:
    print("please just use yes/y or no/n ")
ask_user_str_l = input("did your password contain with lower case alphabet ????")
if ask_user_str_l in switch_case_yes():
    print(">>>>ckuF Your password contain with lower case alphabet <<<<")

elif ask_user_str_l in switch_case_no():
    print(">>>>ckuF Your password will not  contain with  lower case alphabet <<<<")
else:
    print("please just use yes/y or no/n ")
ask_user_str_u = input("did your password contain with upper case alphabet ????")
if ask_user_str_u in switch_case_yes():
    print(">>>>ckuF Your password contain with upper case alphabet  <<<<")
elif ask_user_str_u in switch_case_no():
    print(">>>>ckuF Your password will not  contain with upper case alphabet  <<<<")
else:
    print("please just use yes/y or no/n ")
len1 = len(entry)

if ask_user_int in switch_case_yes():
    if ask_user_sym in switch_case_yes():
        if ask_user_str_l in switch_case_no():
            if ask_user_str_u in switch_case_no():
                checker(list_int_1 + list_sym_1)
        if ask_user_str_l in switch_case_yes():
            if ask_user_str_u in switch_case_no():
                checker(list_int_1 + list_str_l_1 + list_sym_1)
        if ask_user_str_l in switch_case_yes():
            if ask_user_str_u in switch_case_yes():
                checker(list_int_1 + list_str_l_1 + list_str_u_1 + list_sym_1)
        if ask_user_str_l in switch_case_no():
            if ask_user_str_u in switch_case_yes():
                checker(list_int_1 + list_str_u_1 + list_sym_1)
if ask_user_int in switch_case_no():
    if ask_user_sym in switch_case_yes():
        if ask_user_str_l in switch_case_no():
            if ask_user_str_u in switch_case_no():
                checker(list_sym_1)
        if ask_user_str_l in switch_case_yes():
            if ask_user_str_u in switch_case_no():
                checker(list_str_l_1 + list_sym_1)
        if ask_user_str_l in switch_case_yes():
            if ask_user_str_u in switch_case_yes():
                checker(list_str_l_1 + list_str_u_1 + list_sym_1)
        if ask_user_str_l in switch_case_no():
            if ask_user_str_u in switch_case_yes():
                checker(list_str_u_1 + list_sym_1)
if ask_user_int in switch_case_yes():
    if ask_user_sym in switch_case_no():
        if ask_user_str_l in switch_case_no():
            if ask_user_str_u in switch_case_no():
                checker(list_int_1)
        if ask_user_str_l in switch_case_yes():
            if ask_user_str_u in switch_case_no():
                checker(list_str_l_1 + list_int_1)
        if ask_user_str_l in switch_case_yes():
            if ask_user_str_u in switch_case_yes():
                checker(list_str_l_1 + list_str_u_1 + list_int_1)
        if ask_user_str_l in switch_case_no():
            if ask_user_str_u in switch_case_yes():
                checker(list_str_u_1 + list_int_1)
if ask_user_int in switch_case_no():
    if ask_user_sym in switch_case_no():
        if ask_user_str_l in switch_case_no():
            if ask_user_str_u in switch_case_no():
                print("Your pass list is empty!!!!")
        if ask_user_str_l in switch_case_yes():
            if ask_user_str_u in switch_case_no():
                checker(list_str_l_1)
        if ask_user_str_l in switch_case_yes():
            if ask_user_str_u in switch_case_yes():
                checker(list_str_l_1 + list_str_u_1)
        if ask_user_str_l in switch_case_no():
            if ask_user_str_u in switch_case_yes():
                checker(list_str_u_1)