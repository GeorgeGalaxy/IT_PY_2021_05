# number = int(input("Enter number: "))
#
# if number%10==3:
#     print("Number contain 3")
# if number//10==3:
#     print("Number contain 3")
#
# if (number%10)<(number//10):
#     print("First > Second")
# if (number%10)>(number//10):
#     print("First < Second")
# else:
#     print("Equals!")

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

D = b**2 - 4*a*c

if D > 0:
    print(f"x1 = {(-b+((D)**(1/2)))/(2*a)} , x2 = {(-b-((D)**(1/2)))/(2*a)}")
if D == 0:
    print(f"x = {-b/(2*a)}")
if D < 0:
    print("No roots")

