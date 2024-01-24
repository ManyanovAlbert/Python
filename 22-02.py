import random


students = []
while True:
    student = input()
    if student == "":
        break
    students.append(student)
random.shuffle(students)


for i in range(len(students)):
    current_student = students[i]
    secret_friend = students[(i + 1) % len(students)]
    print(f"{current_student} - {secret_friend}")