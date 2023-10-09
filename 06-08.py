N = int(input())
surname_counts = {}
for _ in range(N):
    surname = input().strip()
    if surname in surname_counts:
        surname_counts[surname] += 1
    else:
        surname_counts[surname] = 1
count_of_duplicates = sum(count - 1 for count in surname_counts.values() if count > 1)
print(count_of_duplicates)