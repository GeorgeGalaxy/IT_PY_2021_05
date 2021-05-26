import math

x = 1.0
y = 1.0

while (x <= 2.5) and (y <= 4):
    if (x + y) > 2:
        Func = math.fabs(math.log2(x + y))
        print(f"If x = {x} and y = {y} then Func = {Func}")
    else:
        Func = math.pow(math.sin(x * math.exp(0.1 * y)), 1/3)
        print(f"If x = {x} and y = {y} then Func = {Func}")
    x += 0.5
    y += 1.0
