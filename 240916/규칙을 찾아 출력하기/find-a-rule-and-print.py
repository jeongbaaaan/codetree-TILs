n = int(input())  # 사용자로부터 정수 n 입력

for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1:  # 첫 번째 줄과 마지막 줄
            print('*', end=' ')
        elif j == 0 or j == i or j == n - 1:  # 첫 번째 열, 대각선, 마지막 열에 별
            print('*', end=' ')
        else:
            print(' ', end=' ')  # 나머지는 공백
    print()  # 줄바꿈