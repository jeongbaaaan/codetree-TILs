import math

def find_gcd(x, y):
    return math.gcd(x, y)

def find_divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

def has_common_divisor_in_range(a, b):
    gcd_value = find_gcd(1920, 2880)
    divisors = find_divisors(gcd_value)
    
    # a 이상 b 이하의 공약수가 있는지 확인
    for divisor in divisors:
        if a <= divisor <= b:
            return 1
    return 0

# 입력 받기
a, b = map(int, input().split())

# 결과 출력
print(has_common_divisor_in_range(a, b))