n = int(input())
nums = []
for i in range(n):
    nums.append(input())
for i in range(n - 1):
    for j in range(n - 1 - i):
        if len(nums[j]) > len(nums[j + 1]):
            (nums[j]), (nums[j + 1]) = (nums[j + 1]), (nums[j])
for i in nums:
    print(i)