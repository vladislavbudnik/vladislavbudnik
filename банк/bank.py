import account
import evro

def main():
    rate = int(input("Введите процентную ставку: "))
    money = int(input("Введите сумму: "))
    val = int(input("400-dol, 401-evr, 402-kron, 403-yen: "))
    money2 = evro.evr(money, val)
    period = int(input("Введите период ведения счета в месяцах: "))

    result = account.calculate_income(rate, money2, period)
    print("Параметры счета:\n", "Сумма: ", money2, "\n", "Ставка: ", rate, "\n", "Период: ", period, "\n",
          "Сумма на счете в конце периода: ", result)


if __name__ == "__main__":
    main()
