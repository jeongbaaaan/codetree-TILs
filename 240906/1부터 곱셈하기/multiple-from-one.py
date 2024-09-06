n = int(input())
prom = 1
for i in range(1, 11):
    prom *= i
    if prom >= n:
        print(i)
        break