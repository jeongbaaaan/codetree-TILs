ages = []  # 20대인 사람들의 나이를 저장할 리스트

while True:
    age = int(input())  # 나이를 입력받음
    
    # 20대가 아닌 나이가 입력되면 반복 종료
    if age < 20 or age >= 30:
        break
    
    # 20대인 나이를 리스트에 추가
    ages.append(age)

# 20대 나이들의 평균 계산 (소수점 둘째 자리까지 반올림)
average_age = sum(ages) / len(ages)
print(f"{average_age:.2f}")