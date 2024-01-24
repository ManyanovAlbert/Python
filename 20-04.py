import sys
print(len(list(filter(lambda x: x.strip().startswith('#'), sys.stdin))))