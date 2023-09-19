boys = {"Боря": 175, "Вова": 180, "Дима": 170}
sorted_boys = sorted(boys.items(), key=lambda x: x[1], reverse=True)
for boy, height in sorted_boys:
    print(boy, "-", height, "см")