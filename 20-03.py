import sys
suma = 0
count = 0
for n in sys.stdin:
    suma += int(n)
    count += 1
if count > 0:
    print(suma / count)
else:
    print(-1)


