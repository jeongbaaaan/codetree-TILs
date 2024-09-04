# 입력 받기
a, b = map(int, input().split())

# 조건에 따른 출력
if a > 0:
    print(str(a) * b)
else:
    print(0)