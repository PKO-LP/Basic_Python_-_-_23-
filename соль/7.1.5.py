password = input()

if len(password) >= 3 and ' ' not in password and password[0].isupper() and password[-1].isdigit():
    print(True)
else:
    print(False)