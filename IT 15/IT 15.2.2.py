n = int(input("Enter n: "))

if n > 0:
    if n & n - 1:
        print("NO")
    else:
        print("YES")
