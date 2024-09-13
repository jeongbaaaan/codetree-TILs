def print_check_diamond(n):
    size = 2 * n - 1  # 격자의 크기
    
    # 다이아몬드 윗부분
    for i in range(n):
        line = [' '] * size  # 빈 칸으로 채워진 한 줄 생성
        for j in range(i + 1):
            line[n - i - 1 + 2 * j] = '*'  # 체크 무늬로 별을 배치
        print(''.join(line))
    
    # 다이아몬드 아랫부분
    for i in range(n - 1):
        line = [' '] * size  # 빈 칸으로 채워진 한 줄 생성
        for j in range(n - i - 1):
            line[i + 1 + 2 * j] = '*'  # 체크 무늬로 별을 배치
        print(''.join(line))

# 입력 값 받기
n = int(input())

# 다이아몬드 출력
print_check_diamond(n)