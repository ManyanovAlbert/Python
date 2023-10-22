num_data_strings = int(input())
data_strings = []
for _ in range(num_data_strings):
    data_strings.append(input())
num_search_strings = int(input())
search_strings = []
for _ in range(num_search_strings):
    search_strings.append(input())
result = []
for data_string in data_strings:
    if all(search_string in data_string for search_string in search_strings):
        result.append(data_string)
for data_string in result:
    print(data_string)