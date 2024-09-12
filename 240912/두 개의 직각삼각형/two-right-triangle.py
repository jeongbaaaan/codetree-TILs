def print_symmetric_triangles(n):
    # 총 2n개의 열이 필요합니다.
    total_width = 2 * n

    for i in range(n):
        # 현재 행에서 왼쪽 삼각형의 별
        left_triangle = '*' * (n - i)
        # 현재 행에서 오른쪽 삼각형의 별
        right_triangle = '*' * (n - i)
        # 가운데 공백 부분
        spaces = ' ' * (total_width - 2 * (n - i))

        # 전체 행 조합
        row = left_triangle + spaces + right_triangle
        print(row)

# 입력을 받습니다.
n = int(input())

# 함수를 호출하여 삼각형을 출력합니다.
print_symmetric_triangles(n)