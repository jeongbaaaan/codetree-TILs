a, b, c = map(int, input().split())
# a가 가장 작은 경우
if a <= b and a <= c:
    print(a)
    
# b가 가장 작은 경우
elif b <= a and b <= c:
    print(b)

# c가 가장 작은 경우
else:
    print(c)