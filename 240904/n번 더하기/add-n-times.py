# 입력 받기
a, n = map(int, input().split())

# 반복하면서 결과 출력
for i in range(1, n + 1):
    result = a + i * n
    print(result)