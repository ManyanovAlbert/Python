answer1=input("Любите ли вы котиков? ")
answer2=input("Умеете ли вы программировать? ")
if answer1 not in ["да","нет"] or answer2 not in ["да","нет"]:
    print("Ошибка, да или нет!")
elif answer1 == "да" and answer2 == "нет":
    print("Ооо, вы любитель котиков :}")
elif answer1 == "нет" and answer2 == "да":
    print("Молодцы что не отвлекаетесь от своего хобби!")
elif answer1 == "да" and answer2 == "да":
    print("Вы берете от жизни максимум!")
elif answer1 == "нет" and answer2 == "нет":
    print("Я думал вы поддержите диалог :(")