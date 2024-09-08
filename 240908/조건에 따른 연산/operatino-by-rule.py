n = int(input())
cnt = 0
while True:
    if n % 2 == 0:
        n *3+1
        cnt += 1
    else:
        n *2+2
        cnt += 1
print(cnt)