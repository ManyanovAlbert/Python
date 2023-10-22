s = input() 
max_orel = 0  
orel = 0 

for бросок in s:
    if бросок == 'о':
        orel += 1
        if orel > max_orel:
            max_orel = orel
    else:
        orel = 0
print(max_orel)