n = int(input())
cat = dog = False
for i in range(n):
    text = input()
    if 'кот' in text or 'Кот' in text:
        cat = True
        dog = False
    elif 'Пёс' in text or 'пёс' in text:
        dog = True
        cat = False
if cat:
    print('МЯУ')
else:
    print('Нет')