n = int(input())
soups = ['щи', 'борщ', 'щавелевый суп', 'овсяный суп', 'суп по-чабански']
first_soup_index = 0
for i in range(n):
    soup_index = (first_soup_index + i) % len(soups)
    print(soups[soup_index])