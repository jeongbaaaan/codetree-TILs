b, a = map(int, input().split())  # 두 정수 b와 a를 입력받습니다.

# b부터 a까지 거꾸로 탐색하기 위해 현재 값을 b로 초기화합니다.
current = b

while current >= a:
    if current % 2 == 0:  # 짝수인지 확인합니다.
        print(current, end=' ')  # 짝수라면 출력합니다.
    current -= 2  # 짝수이므로 2씩 감소시킵니다.