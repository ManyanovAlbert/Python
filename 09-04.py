num_of_parts = int(input())
announcement_parts = []
for _ in range(num_of_parts):
    announcement_parts.append(input())
num_of_selected_parts = int(input())
selected_parts = []
for _ in range(num_of_selected_parts):
    part_number = int(input())
    selected_parts.append(announcement_parts[part_number - 1])
for part in selected_parts:
    print(part)
