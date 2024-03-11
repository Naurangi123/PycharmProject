def pattern(num):
    for i in range(num):
        for j in range(num):
            if j == 0 or j == num-1 or j == i or j == num - i -1 :
                print("*",end="")
            else:
                print(" ",end="")
        print()

if __name__ == '__main__':
    pattern(10)