def check_multiples_of_three():
    for _ in range(5):
        number = int(input())  # 5개의 수 입력받기
        if number % 3 != 0:    # 3의 배수가 아닌 경우
            return 0
    return 1

# 결과 출력
print(check_multiples_of_three())