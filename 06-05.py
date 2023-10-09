M, N, K = map(int, input().split())
english_students = {}
german_students = {}
french_students = {}
for _ in range(M + N + K):
    name = input()
    languages = input().split()
    for lang in languages:
        if lang == "английский":
            english_students[name] = True
        elif lang == "немецкий":
            german_students[name] = True
        elif lang == "французский":
            french_students[name] = True
students_with_two_languages = 0
for name in english_students.keys():
    if name in german_students and name not in french_students:
        students_with_two_languages += 1
    elif name in french_students and name not in german_students:
        students_with_two_languages += 1
for name in german_students.keys():
    if name in french_students and name not in english_students:
        students_with_two_languages += 1
if students_with_two_languages > 0:
    print(students_with_two_languages)
else:
    print("NO")