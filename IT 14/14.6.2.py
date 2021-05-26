number = int(input("Enter number: "))
base = int(input("Enter base of number (2-9): "))

if not(2 <= base <= 9):
    print("Error...")
    quit()

newNum = ''

while number > 0:
    newNum = str(number % base) + newNum
    number //= base

print(newNum)


