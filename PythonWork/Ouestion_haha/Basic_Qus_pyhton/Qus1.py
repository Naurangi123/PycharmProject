num = int(input("Enter a number : "))
n = 1
for i in range(num):
    for j in range(2*num):
        if j <= num and j % 2 == 0 :
            print("",end=" ")
        elif(j > num and j % 2 != 0):
            print("*",end="")

        n += 1
    print()