age1, gender1 = input().split()
age1 = int(age1)

# 두 번째 사람의 나이와 성별을 입력받습니다.
age2, gender2 = input().split()
age2 = int(age2)

# 조건을 확인합니다.
if (age1 >= 19 and gender1 == 'M') or (age2 >= 19 and gender2 == 'M'):
    print(1)
else:
    print(0)