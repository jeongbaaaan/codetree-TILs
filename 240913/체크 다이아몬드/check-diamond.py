def print_check_diamond(n):
    size = 2 * n - 1  # 격자의 크기
    for i in range(size):
        # 중앙으로부터의 거리를 구함
        row = abs(n - i - 1)
        # 별의 개수는 n-row
        stars = n - row
        # 출력할 문자열 생성
        line = [' '] * size
        for j in range(stars):
            # 체크 무늬로 별을 그리기 위해 짝수 열에만 별을 넣음
            line[n - stars + 2 * j - 1] = '*'
        print(''.join(line))

# n = 3일 때 다이아몬드 출력
n = 3
print_check_diamond(n)