import datetime

day = int(input())
days = datetime.datetime.now()
res = datetime.timedelta(days=day) + days
print(res.day, res.month)