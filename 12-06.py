text = input().upper().split()
for i in range(len(text)):
    print('-'.join(text[i]), end=' ')