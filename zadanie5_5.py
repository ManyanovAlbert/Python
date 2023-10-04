line_numbers = 1
foundcat = False
while True:
    line = input()
    if line == 'СТОП':
        break
    if 'кот' in line:
        foundcat = True
        break
    line_numbers += 1
if foundcat:
    print(line_numbers)
else:
    print(-1)
