def print_reflected_square(n):
    # 1. 정사각형 배열 생성
    matrix = [[(i+1) * (j+1) for j in range(n)] for i in range(n)]
    
    # 2. 좌우반전된 정사각형 출력
    for row in matrix:
        print(" ".join(map(str, row[::-1])))  # 각 행을 좌우반전하여 출력

# 입력 받기
n = int(input())

# 함수 호출하여 출력
print_reflected_square(n)