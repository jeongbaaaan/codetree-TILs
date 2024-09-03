b, a = map(int, input().split())  # 두 정수를 입력받아 b, a에 저장합니다.

# b부터 a까지의 홀수를 내림차순으로 출력합니다.
for i in range(b, a - 1, -1):  # b에서 a까지 거꾸로 반복합니다.
    if i % 2 == 1:  # 홀수인지 확인합니다.
        print(i, end=' ')