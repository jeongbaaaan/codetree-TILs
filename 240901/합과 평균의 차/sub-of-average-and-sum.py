# 세 정수를 입력받습니다.
a, b, c = map(int, input().split())

# 세 정수의 합을 구합니다.
total_sum = a + b + c

# 세 정수의 평균을 구합니다. 평균은 합을 3으로 나눈 값입니다.
average = total_sum // 3

# 합에서 평균을 뺀 값을 구합니다.
difference = total_sum - average

# 결과를 출력합니다.
print(total_sum)
print(average)
print(difference)