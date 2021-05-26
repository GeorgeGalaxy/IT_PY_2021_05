n = int(input("Enter n: "))
k = int(input("Enter k: "))

area_1 = (1 << k) - 1
area_1 = ~((1 << k) - 1)

print(f"Result = {n & area_1}")



