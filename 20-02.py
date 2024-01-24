if all([any([input()[-1] == '5' for student2 in range(int(input()))]) for student1 in range(int(input()))]):
    print('ДА')
else:
    print('НЕТ')