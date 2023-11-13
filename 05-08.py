kot_sum = count = str_num = 0
kot = False
while True:
    count += 1
    text = input()
    if 'СТОП' in text:
        break
    if kot:
        continue
    elif 'кот' in text or 'Кот' in text:
        kot_sum += 1
        str_num = count
        kot = True
if kot:
    print(kot_sum, str_num)
else:
    print(kot_sum, '-1')



