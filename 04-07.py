n = int(input("Введите натуральное число: "))
divisor_count = 0
for i in range(1, n + 1):
    if n % i == 0:
        divisor_count += 1
if divisor_count == 2:
    prime_status = "ПРОСТОЕ"
else:
    prime_status = "НЕТ"
print(prime_status)
