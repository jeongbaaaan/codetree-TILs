# 정수 n 입력 받기
n = int(input())

# 첫 번째 줄은 별을 n개 출력
print("* " * n)

# 두 번째 줄부터 마지막 전 줄까지
for i in range(1, n - 1):
    print("* " + "  " * (i - 1) + "* " + "  " * (n - i - 2) + "* ")

# 마지막 줄은 별을 n개 출력
if n > 1:
    print("* " * n)