# 물건의 가격 목록을 딕셔너리로 정의합니다.
items = {
    "book": 3000,
    "mask": 1000
}

# 가지고 있는 돈 n을 입력받습니다.
n = int(input())

# 살 수 있는 물건 중 가장 비싼 물건을 찾습니다.
max_item = "no"  # 초기값을 "no"로 설정합니다.
max_price = 0

# 딕셔너리를 순회하며 조건에 맞는 가장 비싼 물건을 찾습니다.
for item, price in items.items():
    if price <= n and price > max_price:
        max_item = item
        max_price = price

# 결과를 출력합니다.
print(max_item)