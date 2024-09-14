# 정수 n 입력 받기
n = int(input())

# 2 * n번 반복
for i in range(2 * n):
    if i == 2 * n - 1:  # 마지막 줄일 때는 무조건 n개의 별 출력
        print("* " * n)
    elif i % 2 == 0:  # 짝수 줄 (0, 2, 4,...): n - i//2 개의 별 출력
        print("* " * (n - i // 2))
    else:  # 홀수 줄 (1, 3, 5,...): 1 + i//2 개의 별 출력
        print("* " * (1 + i // 2))