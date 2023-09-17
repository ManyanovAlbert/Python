answer1=input("Введите логин: ")
answer2=input("Введите резервную почту: ")
if answer1 in ["@"]:
    print("Введите корректный логин")
elif "@" not in answer2:
    print("Введите корректный адрес почты :}")
else:
    print("ОК")
