nums_i = [int(i) for i in input().split()]
slice = [int(i) for i in input().split()]
for i in slice:
    if i < 0 or i > len(nums_i):
        print('Введенные числа не должны быть меньше нуля или превышать количество элементов в наборе')
print(sum(nums_i[slice[0]:slice[1] + 1:]))