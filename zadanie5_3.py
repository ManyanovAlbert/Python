line_numbers = 0
foundcat = False
first_cat=-1
while True:
    line = input()
    line_numbers += 1
    if line == 'СТОП':
        break
    if not foundcat and ('кот' in line or 'Кот' in line):
       foundcat = True
       first_cat= line_numbers

    if line =='СТОП':
        break

if first_cat != -1:
    print(first_cat)
else:
    print(-1)
