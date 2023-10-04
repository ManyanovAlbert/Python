n= int(input())
foundcat=False

for i in range(n):
    text=input()
    if 'Кот' in text or'кот' in text:
        foundcat=True
        break
if foundcat:
    print('Мяу')
else:
    print('нет')
