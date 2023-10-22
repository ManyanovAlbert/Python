one_word = None
two_word = None
while True:
    word = input()
    if word == "стоп":
        break

    if one_word is None or len(word) < len(one_word):
        one_word = word
    if two_word is None or len(word) > len(two_word):
        two_word = word
identical_letters = all(letter in two_word for letter in one_word)

if identical_letters:
    print("ДА")
else:
    print("НЕТ")
