# 세 정수를 입력받습니다.
a, b, c = map(int, input().split())

# 입력받은 세 정수를 리스트로 만들고 정렬합니다.
numbers = [a, b, c]
numbers.sort()

# 정렬된 리스트에서 중앙값을 출력합니다.
print(numbers[1])