#1
def func1():
    print('Hello world!')
    name = input('Введите имя')
    print('Привет, ' + name)
    print(5 + 7)
    print(4 * 5)
    print(4 ** 3)
    x = input('Введите х') # возвращается строка, не число
    x=float(x) # преобразуем строку в вещественное число
    y=x**2+3*x-100
    print(y)

#2
def func2():
    string = 'строка'
    _integer = 12
    _float_1 = 3.14
    _float_2 = -2.7e-3
    _boolean = True
    print( type(_boolean) ) # <class 'bool'>
    print(2+1 > 3*4)
    print( not (3>1 and False) )
    empty_list = [] # пустойсписок
    _list = [1, 3.14, 'свет', True, []] # списоксэлементами
    empty_list.append( 12 ) # добавлениеэлемента
    empty_list.append( [2.7, 3] )
    print( empty_list, _list )
    _list[0] = 'перезаписываем первый элемент на этот текст'
    print( _list, empty_list[1] )
    a = 12 + 3.14
    print( type(a) )
    print(9/3 > 2*3 or not(12 != 3**2+3 and 57-24 > 30) )

#3

def func3():
    import math as m
    a = m.sin(m.pi/2)
    b = m.sqrt( 16 )
    c_1 = m.e**2
    c_2 = m.exp(2)
    d_1 = m.log(8, 2)
    d_2 = m.log2(8)
    e_1 = m.ceil(3.14)
    e_2 = m.ceil(2.7)
    a, b, c = 3, -10, 1
    D = b ** 2 - 4 * a * c
    x_1 = (-b - m.sqrt(D)) / (2 * a)
    x_2 = (-b + m.sqrt(D)) / (2 * a)
    print(x_1, x_2)
    x = float(input("Введите x: "))
    print(m.log2(7 * x) * m.cos(x / 3))
#4
def func4():
    print('Введите число в десячиной системе счисления')
    a = int(input())
    print('Двоичная: ', bin(a))
    print('Восьмеричная: ', oct(a))
    print('Шестнадцатиричная: ',hex(a))
#5
def func5():
    x = int(input('Введите х'))  # преобразуем строку в целое число
    if x < 0: # если введенное число меньше нуля
        x = -x
    print(x)
    x = int(input())
    y = int(input())
    if x > 0 and y > 0:
        print("Первая четверть")
    elif x > 0 and y < 0:
        print("Четвертая четверть")
    elif y > 0:
        print("Вторая четверть")
    else:
        print("Третья четверть")

#6
def func6():
    for i in [1, 2, 3, 4, 5]:
        a = i * i
    print(a)
    for i in range(1, 6):
        print("Hello")
    n = int(input())
    i = 1
    while i ** 2 < n:
        print(i ** 2)
        i += 1
    n = [1, 2, 3, 7, 6, 4, 5, 8]  # пример списка
    for x in n:
        if x == 237:
            break
        elif x % 2 == 0:
            print(x)
    s = input()
    for i in s:
        if (i == ' '): continue
    print(i, end='')  # end = '' не переводит на новую строку

func1()
func2()
func3()
func4()
func5()
func6()