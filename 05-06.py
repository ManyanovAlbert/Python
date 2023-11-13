count = 0
total = 0
sum_10 = False
while True:
    count += 1
    num = int(input())
    total += num
    if num == 0:
        break
    if sum_10:
        continue
    if total == 10:
        print(count)
        sum_10 = True
