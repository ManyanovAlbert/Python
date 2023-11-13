word = input()
index = int(input())
if index > len(word):
    print("Ошибка")
else:
    print(word[index - 1])