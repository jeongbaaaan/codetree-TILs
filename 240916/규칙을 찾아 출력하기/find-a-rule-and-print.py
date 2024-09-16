n = int(input())

for i in range(n):
    if i % 2 == 0:
        # 짝수 줄: 별을 n개 출력
        print('* ' * n)
    else:
        # 홀수 줄: 별과 공백 처리
        stars = '* ' * (i // 2 + 1)
        spaces = ' ' * (2 * (n - (i // 2 + 1) - 1))
        print(stars + spaces + '* ' * (i // 2))