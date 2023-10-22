size = int(input())
for row in range(size, 0, -1):
    for col in range(1, size + 1):
        cell = f"{chr(col + 64)}{row}"
        print(cell, end=" ")
    print()
