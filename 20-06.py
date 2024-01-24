import sys
data = list(map(str.strip, sys.stdin))
print(*sorted(data, key=lambda x: sum([ord(i) - ord('A') + 1 for i in x.upper()])), sep='\n')