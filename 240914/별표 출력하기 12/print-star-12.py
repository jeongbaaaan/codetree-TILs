# 정수 n 입력 받기
n = int(input())

# 첫 번째 줄: n개의 별을 출력
print("* " * n)

# 두 번째 줄부터 마지막 줄까지
for i in range(1, n):
    # 공백은 i * 2개, 출력할 별의 개수는 n - i개
    print(" " * (i * 2) + "* " * (n - i))