a, b = map(int, input())
prod = 1
for i in range(1, b+1):
    if i % a == 0:
        prod *= 1
print(prod)