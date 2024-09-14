n = int(input())

for i in range(2*n):
    if i % 2 == 0:
        print("* " * (n-i//2))
    else:
        print("* " * (1+i//2))