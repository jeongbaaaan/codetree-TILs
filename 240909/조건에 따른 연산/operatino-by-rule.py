def find_cnt(n):
    cnt = 0
    while n < 1000:
        if n % 2 == 0:
            n = n * 3 + 1
        else:
            n = n * 2 + 2
        cnt += 1
    return cnt

# 입력 받기
n = int(input())

# cnt 값 출력
print(find_cnt(n))