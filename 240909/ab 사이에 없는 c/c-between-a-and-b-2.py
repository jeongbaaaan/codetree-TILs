a, b, c = map(int, input().split())
satisfied = False
for i in range(a, b+1):
    if c % a != 0 or c % b != 0:
        satisfied = True

if satisfied == True:
    print("YES")
else:
    print("NO")