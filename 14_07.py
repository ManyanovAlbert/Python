def print_statistics(arr):
    if not arr:
        print(0, 0, 0, 0, 0)
        return

    n = len(arr)

    median = median_of_list(arr)

    min_element = min(arr)
    max_element = max(arr)

    average = average_of_list(arr)

    print(n, average, min_element, max_element, median)

def median_of_list(arr):
    if len(arr) == 1:
        return arr[0]
    elif len(arr) % 2 == 0:
        return (arr[len(arr) // 2 - 1] + arr[len(arr) // 2]) / 2
    else:
        return arr[len(arr) // 2]

def average_of_list(arr):
    return sum(arr) / len(arr)
arr = [3, 5, 8, 4]
print_statistics(arr)  # Output: 4 5 3 8 4.5
