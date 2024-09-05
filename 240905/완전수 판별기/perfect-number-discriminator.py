n = int(input())
sum_n = 0

# 1부터 n-1까지의 수 중에서 약수를 찾음
for i in range(1, n):
    if n % i == 0:
        sum_val += i

if sum_n == n:
    print("P")
else:
    print("N")