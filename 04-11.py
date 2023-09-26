average = 0
sum = 0
for i in range(int(input())):
    iq = int(input())
    sum += iq
    average = sum/(i+1)
    if iq == average:
        print('0')
    elif iq > average:
        print('>')
    else:
        print('<')