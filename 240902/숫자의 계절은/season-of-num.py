# 변수 선언, 입력
m = int(input())

# 출력
if m >= 12 or m <= 2:
	print("Winter")
elif m <= 5:
	print("Spring")
elif m <= 8:
	print("Summer")
else:
	print("Fall")