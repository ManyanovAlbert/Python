n = int(input())
pupils = []
for i in range(n):
    pupils.append(input())
for i in pupils:
    print(i)
print('')
for i in pupils:
    if '4' in i or '5' in i:
        print(i)
