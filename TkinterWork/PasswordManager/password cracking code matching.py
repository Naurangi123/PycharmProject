from random import *
list = [ '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a','b','c','d','e','f','g','h','i',
         'j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] # giving it a list

passlength = int(input('Length of string: ')) # length of code or no of objects
aspass = '' # empty string acts as assumed password
passs = input('Please input password ') # he infamous password
b = [] # the list that will stores randomly generated passwords as values
attempt = 0
digits = 0
o=True
while o:
    for k in range(0, passlength): # run this loop as many times as the length of password
        x = str(random.choice(list))#the attempted upon digit in the password
        aspass += x
        digits += 1 # counts the step the cracker is on
        #print(aspass)
        if(len(aspass) > passlength or aspass in b):
            digits = 0
            attempt += 1
            break
        else:
            continue
        #b.append(aspass)
    if(aspass == passs):
        break
        o = False
        end()
    else:
        b.append(aspass)
        aspass = ''
        continue