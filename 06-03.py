M = int(input())
N = int(input())
e_students = set()
g_students = set()
for _ in range(M):
    name = input()
    e_students.add(name)
for _ in range(N):
    name = input()
    g_students.add(name)
only_english = e_students - g_students
only_german = g_students - e_students
if len(only_english) + len(only_german) > 0:
    print(len(only_english) + len(only_german))
else:
    print("NO")