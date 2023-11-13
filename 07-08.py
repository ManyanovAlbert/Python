num = int(input())
while num <= 1000000000:
    factor = int(str(num)[0])
    num *= factor
    if factor == 1:
        break
print(num)