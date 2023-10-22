d = int(input())
results = []
for i in range(d):
    line = input()
    if "кот" in line:
        index = line.index("кот") + 1
        results.append((i + 1, index))
for result in results:
    print(result[0], result[1])
