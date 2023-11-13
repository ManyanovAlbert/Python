word_2 = input()
word_3 = input()
while word_2[-1] == word_3[0]:
    word_2 = input()
    word_3 = input()
if word_2[-1] != word_3[0]:
    print(word_3)
