# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег
account = 0
count_operations = 0
withdrawal_percentage = 1.5


def transaction(mod):
    while True:
        money = int(input(
            '\nВведите сумму на которую хотите снять или добавить\nНо помните сумма пополнения и снятия кратны 50: '
        ))
        if money % 50 == 0:
            if mod == 1:
                top_up(money)
            else:
                withdraw_money(money)
        else:
            print('Сумма не кратна 50')
        if int(input('\nНажмите 1, если хотите снова пополнить или снять со счета или 0 если нет: ')) == 0:
            print()
            break


def top_up(money):
    global account
    account += money
    show_account()


def show_account():
    print(f"\nВаш счет: {account}")


def withdraw_money(money):
    global account, withdrawal_percentage, count_operations
    wealth_tax = 0
    persent = money * 1.5 / 100

    if persent > 600:
        persent = 600
    elif persent < 30:
        persent = 30

    if account > 5000000:
        wealth_tax = money * 10 / 100

    if account < money + persent + wealth_tax:
        print(f"На счете не хватает денег. С коммиссией вычет будет равен: {money + persent + wealth_tax}")
    else:
        account -= money + persent + wealth_tax
    show_account()


def main():
    global count_operations
    while True:
        choice = int(input('Нажмите 1, чтобы пополнить баланс\n'
              'Нажмите 2, чтобы снять деньги со счёта\n'
              'Нажмите 3, чтобы посмотреть ваш счет\n'
              'Нажмите 4, чтобы завершить все операции(logout)\n'
                           '- '))
        match choice:
            case 1:
                transaction(choice)
            case 2:
                transaction(choice)
            case 3:
                show_account()
            case 4:
                break
            case _:
                print("Такой команды, введите пожалуйста команду из инструкции")
        count_operations += 1
    print("Спасибо, что с нами")


if __name__ == '__main__':
    main()
