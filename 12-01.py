n = int(input())
for i in range(n):
    line = input()
    if "кот" in line:
        start_index = line.index("кот")
        print(f"Line {i+1}: {start_index+1}")