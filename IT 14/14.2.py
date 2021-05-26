strange = [[],1]

print(type(strange))

x = True
y = True

if ((x or y) and (not x or y) and not(x and y)):
    print (f"x = {x} ,y = {y}")

x = False
y = True

if ((x or y) and (not x or y) and not(x and y)):
    print (f"x = {x} ,y = {y}")

x = False
y = False

if ((x or y) and (not x or y) and not(x and y)):
    print (f"x = {x} ,y = {y}")

x = True
y = False

if ((x or y) and (not x or y) and not(x and y)):
    print (f"x = {x} ,y = {y}")

list_1 = []

list_1.append(input("Enter 1 element:"))
list_1.append(input("Enter 2 element:"))
list_1.append(input("Enter 3 element:"))
list_1.append(input("Enter 4 element:"))

print(list_1)
