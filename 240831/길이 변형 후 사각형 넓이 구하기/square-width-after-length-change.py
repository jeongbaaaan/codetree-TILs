# 변수 선언, 입력
inp = input()
arr = inp.split()
w = int(arr[0])
h = int(arr[1])

w += 8
h *= 3

# 출력
print(w)
print(h)
print(w * h)