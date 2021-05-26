number = int(input("Enter number 1: "))

i = 1

if number>=2:
    while i<=number:
        i = i + 1
        if number%i == 0:
            print(i)
            break


S = 0

N = int(input("Enter N: "))

def summ(x):

    global S

    if(x)!=0:
        S += x
        summ(x-1)
    else:
        return

summ(N)

print(f"Summ = {S}")

def IsPrime(n):
    d = 2
    while n % d != 0:
        d += 1
    return  d==n

number_IsPrime = int(input("Enter number for checking prime: "))

print(IsPrime(number_IsPrime))
