from math import *
a = float(input('input a: '))
b = float(input('input b: '))
h = float(input('input h: '))
x = a
value = 0
func = "value = cos(e*x)**3 + sin(fabs(x))"
func1 = compile(func, "compiledfunc", 'exec')
while x <= b:
    exec(func1)
    print(f'x = {x}, value = {value}')
    x += h
