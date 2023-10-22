n = int(input())  
s = list(map(int, input().split())) 

for i in range(n - 1):
    print(s[i] + s[i + 1])