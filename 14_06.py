def print_average(arr):
    if not arr:
        print(0)
    else:
        total = sum(arr)
        average = total / len(arr)
        print(average)
arr = [1, 2, 3, 4, 5]
print_average(arr)  # Output: 3.0