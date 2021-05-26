# k, n = map(int, input("Enter k and n: ").split())
k = int(input("Enter k: "))
n = int(input("Enter n: "))

result = (1 << k) + (1 << n)

print(f"2^{k} + 2^{n} = {result}")
