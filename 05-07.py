n = int(input())
change = False
count_change = 0
for i in range(n):
    text = input()
    if 'Меняем' in text:
        count_change += 1
        if count_change % 2 == 0:
            change = False
        else:
            change = True
        continue
    if change:
        if 'С кем война?' in text:
            print('Остазия')
        elif 'С кем мир?' in text:
            print('Евразия')
    else:
        if 'С кем война?' in text:
            print('Евразия')
        elif 'С кем мир?' in text:
            print('Остазия')