M = int(input())
available_dishes = set(input().split())
N = int(input())
never_cooked_dishes = []
for _ in range(N):
    num_dishes_in_day = int(input())  
    dishes_in_day = set(input().split())  
    already_cooked_dishes = set.intersection(available_dishes, dishes_in_day)
    available_dishes -= already_cooked_dishes
for dish in available_dishes:
    print(dish)