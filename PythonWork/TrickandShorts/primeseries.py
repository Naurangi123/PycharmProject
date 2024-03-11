def prime(n):
    x=1
    for i in range(2,n):
        if n%i==0:
            x=0
            break
        else:
            x=1
    return x

num=int(input("Enter the Number"))
i=2
c=1
while True:
    if prime(i):
        print(i)
        c+=1
    i+=1
    if c>num:
        break