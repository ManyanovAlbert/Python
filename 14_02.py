def space_game(text):
    count = text.count(' ')
    if count % 2 == 0:
        print("Вы выиграли")
    else:
        print("Вы проиграли")
space_game(input())