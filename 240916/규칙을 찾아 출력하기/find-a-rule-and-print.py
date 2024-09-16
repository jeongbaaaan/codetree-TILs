n = int(input())  # 사용자로부터 정수 n 입력

# 첫 번째 줄은 n개의 별 출력
print("* " * n)

# 두 번째 줄부터 n-1번째 줄까지
for i in range(1, n):
    print("* " * i + "*" + " " * (2 * (n - i - 1)) + "*")

# 마지막 빈 줄 추가
print()