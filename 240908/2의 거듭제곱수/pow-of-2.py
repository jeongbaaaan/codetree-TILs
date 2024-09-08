n = int(input())
prod = 1
x = 0
while true:
    if n == prod:
        break
    prod *= 2
    x += 1
print(x)