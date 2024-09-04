a, b = map(int, input().split())  # 두 정수 a와 b를 입력받습니다.

# 현재 값을 a로 초기화
current = a

# while문을 이용하여 a부터 b까지 반복
while current <= b:
    if current % 2 == 0:  # 짝수인지 확인합니다.
        print(current, end=' ')  # 짝수라면 출력합니다.
    current += 2  # 짝수이므로 2씩 증가시킵니다.