# 사용자로부터 N을 입력받습니다.
N = int(input())

# N개의 정수를 저장할 리스트를 초기화합니다.
numbers = []

# N개의 정수를 입력받아 리스트에 저장합니다.
for _ in range(N):
    num = int(input())
    numbers.append(num)

# 홀수이면서 3의 배수인 수들만 필터링하여 출력합니다.
for num in numbers:
    if num % 2 == 1 and num % 3 == 0:
        print(num)