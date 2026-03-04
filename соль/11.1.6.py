def buy():
    def check_balance():
        if balance >= price:
            return True
        else:
            return False

    if check_balance():
        print("Покупка совершена")
    else:
        print("Недостаточно средств")


# Код ниже не меняйте, проанализируйте, и используйте для создания функций:
balance = int(input())  # баланс покупателя
price = int(input())  # цена за товар
buy()  # процесс покупки