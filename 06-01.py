one_list = set()
two_list = set()
while True:
    number = input()
    if number == "":
        break
    one_list.add(int(number))
input()
while True:
    number = input()
    if number == "":
        break
    two_list.add(int(number))
intersection = one_list.intersection(two_list)
if intersection:
    print(*intersection)
else:
    print("EMPTY")