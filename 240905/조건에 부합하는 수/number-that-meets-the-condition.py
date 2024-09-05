# 입력 받기
a = int(input())

# 1부터 a까지 반복하면서 조건을 확인
for i in range(1, a + 1):
    # 조건을 모두 만족하지 않는 경우 출력
    if not (i % 2 == 0 and i % 4 != 0) and not (i // 8 % 2 == 0) and not (i % 7 < 4):
        print(i, end=" ")