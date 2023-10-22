text = input() 
for char in text: 
    if not (char.islower() or char.isdigit() or char == '_'):
        print("Неверный символ:", char)
        break
else:
    print("OK")