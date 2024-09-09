a, b, c = map(int, input().split())

d = False

for i in range(a, b + 1):
	# a에서 b사이의 값 중 c의 배수가 있는지 확인합니다.
	if i % c == 0:
		d = True


# 출력
if d == True:
	print("YES")
else:
	print("NO")