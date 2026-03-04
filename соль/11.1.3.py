# Принимаем логин и пароль
login = input()
password = input()

# Создаем функцию с позиционными и именованными параметрами
def check_login_password(login, password, true_login="admin", true_password="admin"):
    if login == true_login and password == true_password:
        print(True)
    else:
        print(False)

# Вызываем функцию
check_login_password(login, password)