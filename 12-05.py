n = int(input()[1:])
a = [input() for i in range(n)]
b = []
for i in a:
    if '#' in i:
        a.append(i[:i.find("#")].rstrip())
    else:
        b.append(i.rstrip())
for i in b:
    print(i)

