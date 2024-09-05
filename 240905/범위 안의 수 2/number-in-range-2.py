sum_val = 0
cnt = 0
for _ in range(10):
    num = int(input())
    if num >= 0 and num <= 200:
        sum_val += num
        cnt += 1

avg = sum_val / cnt
print(f"{sum_val} {avg:.1f}")