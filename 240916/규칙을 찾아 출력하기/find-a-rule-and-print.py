n = int(input())

print("* " * n)

for i in range(1, n-1):
    print("* " * i, " " * (n - i), "*")