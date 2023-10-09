n = int(input())
cities = set()

for _ in range(n):
    city = input().strip()
    cities.add(city)

new_city = input().strip()

if new_city in cities:
    print("OK")
else:
    print('TRY ANOTHER')