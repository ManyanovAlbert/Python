num = filter(lambda x: x % 9 == 0, range(10, 100))
cypher = map(lambda x: x ** 2, num)
res = sum(cypher)
print(res)