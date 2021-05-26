import math

x = float(input("Enter x: "))
y = float(input("Enter y: "))

sin_x_y = math.sin(x+y)

func = 0.0

if sin_x_y >= 0.5:
    funct = x**3 + y**1.5
    print(f"Function = {funct}")

if (sin_x_y > (-0.5)) and (sin_x_y < (0.5)):
    funct = 3 * math.log(math.fabs(x * y), 3)
    print(f"Function = {funct}")

if sin_x_y <= -0.5:
    funct = math.atan(math.pow(math.fabs(x - y)),1/3) * x*math.exp(y)
    print(f"Function = {funct}")
