a, b = map(int, input().split())

# a부터 b까지의 수 중 홀수만 출력
for num in range(a, b+1):  # a 부터 b까지
		if num % 2 == 1:  
				print(num, end=" ")