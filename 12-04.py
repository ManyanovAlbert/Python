nums = [int(i) for i in input().split()]
slice = [int(i) for i in input().split()]
for i in slice:
    if i < 0 or i > len(nums):
        print('Введенные числа не должны быть меньше нуля или превышать количество элементов в наборе')
for i in range(slice[1] + 1):
    nums[i] *= nums[i]
print(sum(nums[slice[0]:slice[1] + 1:]))