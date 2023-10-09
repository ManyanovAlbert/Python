M = int(input())
all_present = set(input().strip() for _ in range(int(input())))
for _ in range(M - 1):
    current_present = set(input().strip() for _ in range(int(input())))
    all_present.intersection_update(current_present)
for name in all_present:
    print(name)