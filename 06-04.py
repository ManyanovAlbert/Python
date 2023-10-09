M, N = map(int, input().split())

english_students = set()
german_students = set()

for _ in range(M + N):
    last_name = input()
    language = input()

    if language == "English":
        english_students.add(last_name)
    elif language == "German":
        german_students.add(last_name)

students_only_one_language = english_students.symmetric_difference(german_students)

if len(students_only_one_language) > 0:
    print(len(students_only_one_language))
else:
    print("NO")