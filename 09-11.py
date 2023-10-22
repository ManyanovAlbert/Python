num_whitelist_items = int(input())
whitelist = set()
for _ in range(num_whitelist_items):
    item = input()
    whitelist.add(item)
num_queries = int(input())
queries = []
for _ in range(num_queries):
    query = input()
    queries.append(query)
filtered_queries = []
for query in queries:
    if query in whitelist:
        filtered_queries.append(query)
for query in filtered_queries:
    print(query)