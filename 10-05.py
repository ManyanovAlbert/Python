n = int(input())
soliders = []
for i in range(n):
    soliders.append(input())
rarity = int(input())
repeat = int(input())
for i in range(repeat):
    del soliders[rarity - 1::rarity]
    for j in soliders:
        print(j)
    print('')