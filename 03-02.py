pass1=input()
pass2=input()
if len(pass1) < 8:
    print("короткий")
elif pass1 == pass2:
    print("ок")
else:
    print("НЕТ совпадения")