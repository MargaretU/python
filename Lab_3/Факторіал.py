def fac(n):
    return fac(n - 1) * n if n > 0 else 1


print("Input n=")
n = int(input())
print(n, "!=", fac(n))