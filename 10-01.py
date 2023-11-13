n = int(input())
nums = []
flag = False
for i in range(n):
    nums.append(int(input()))
prod = int(input())
for i in range(len(nums)):
    if len(nums) - i == 1:
        break
    if nums[i] * (nums[i + 1]) == prod:
        flag = True
if flag:
    print('Yes')
else:
    print('No')


