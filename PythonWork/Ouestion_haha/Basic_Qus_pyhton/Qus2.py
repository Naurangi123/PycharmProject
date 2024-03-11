def checkPrime(num):
    for i in range(2,num):
        if num % i == 0 :
            return False
    return True
def checkPrimeSum(sum):
    for i in range(sum):
        for j in range(sum):
            if i + j == sum and checkPrime(i) and checkPrime(j):
                return True
    return False

if __name__ == '__main__':
    print(checkPrimeSum(14))