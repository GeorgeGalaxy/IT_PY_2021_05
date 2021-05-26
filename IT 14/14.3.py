import math as m

x = float(input("Enter x: "))

F = (m.tan(((m.sin(x*2))*(m.cos(x)))/(x*(m.e**x))))**(m.log(x,7))

print(f"F = {F}")

list_binary = [0,1,0,1,1,1,0]

last_number = int(list_binary[list_binary[len(list_binary)-1]])

print(f"Last bite = {last_number}")