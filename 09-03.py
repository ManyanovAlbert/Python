num_of_strings = int(input())
strings = []
for _ in range(num_of_strings):
    strings.append(input())

letter_number = int(input())
result = ""
for string in strings:
    if len(string) >= letter_number:
        result += string[letter_number - 1]
print(result)
