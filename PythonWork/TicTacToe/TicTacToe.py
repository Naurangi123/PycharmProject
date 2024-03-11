import random

positions=[i for i in range(1,10)]
occupied=[]

def gameBoard():
    print("""
      {}|{}|{}
      --------
      {}|{}|{}
      --------
      {}|{}|{}
    
    """.format(positions[0],positions[1],positions[2],
               positions[3],positions[4],positions[5],
               positions[6],positions[7],positions[8]))

def userMove(ch):
    pos=int(input("Enter your Position:"))
    positions[pos-1]=ch
    occupied.append(pos)

def cpuMove(ch):
    num=random.randint(1,9)
    if num in occupied:
        cpuMove(ch)
    else:
        print("CPU Moved at:",num)
        positions[num-1]=ch
        occupied.append(num)


def cpuMode(cpu):
    pass


def main():
    gameBoard()
    user_ch=input("Enter your choice:0/X:")
    if user_ch=="0":
        cpu_="X"
    else:
        cpu="0"
    while True:
        userMove(user_ch)
        gameBoard()
        cpuMode(cpu)
        gameBoard()

main()
