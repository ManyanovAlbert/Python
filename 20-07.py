import sys


def fl(x):
    ind, com = x
    return 'Line {}: {}'.format(ind, com.lstrip('#').strip())


lin = map(str.lstrip, sys.stdin)
c = filter(lambda d: d[1].startswith('#'), enumerate(lin, 1))
n = map(fl, c)
print(*n, sep='\n')
