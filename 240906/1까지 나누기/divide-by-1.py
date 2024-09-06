# 입력으로 정수 n을 받습니다.
n = int(input())

# 나눗셈 횟수를 카운트할 변수
count = 0

# 나누는 수를 1부터 시작합니다.
divisor = 1

# 몫이 1 이하가 될 때까지 나눗셈을 반복합니다.
while n > 1:
    n = n // divisor 
    count += 1
    divisor += 1
      # n을 divisor로 나눈 몫으로 업데이트합니다.

# 결과를 출력합니다.
print(count)