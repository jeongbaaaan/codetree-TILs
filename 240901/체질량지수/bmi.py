h, w = map(int, input().split())
bmi = w*10000 // (h*h)

print(bmi)
if bmi >= 25:
		print("Obesity")