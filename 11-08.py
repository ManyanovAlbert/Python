url = input().split('&')
s = input()
value = []
flag = False
for i in url:
    if s in i:
        for j in i:
            if j == '=':
                flag = True
            if flag:
                if j != '=':
                    value.append(j)
for i in value:
    print(i, end='')
