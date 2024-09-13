n = int(input())  # 정수 n 입력받기

for i in range(1, n + 1):  # 1부터 n까지 반복
    if i % 2 == 1:  # 홀수 번째 줄
        print("*")
    else:  # 짝수 번째 줄
        print("* " * i)  # 해당 줄 번호(i)만큼 * 출력