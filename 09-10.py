n = int(input())
numbers = []
for _ in range(n):
    numbers.append(int(input()))
p = int(input())
q = int(input())
sum = 0
for i in range(p-1, q):
    sum += numbers[i]
print(sum)