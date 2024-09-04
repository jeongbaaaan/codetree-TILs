# 입력 받기
a, n = map(int, input().split())

# 반복하면서 결과 출력
for _ in range(n):
    a += n
    print(a)