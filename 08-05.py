d = int(input())
advice_list = []
for _ in range(d):
    advice = input()
    if advice[:3].lower() == "не ":
        advice = advice[3:]
    advice_list.append(advice)
for advice in advice_list:
    print(advice)
