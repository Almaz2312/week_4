"""
Пользователь делает вклад в размере a рублей сроком на years лет под 10% годовых (каждый год размер его вклада увеличивается на 10%. Эти деньги прибавляются к сумме вклада, и на них в следующем году тоже будут проценты).
Написать функцию bank, принимающая аргументы a и years, и возвращающую сумму, которая будет на счету пользователя.
"""

def depos(money, years):
    for i in range(years):
        money = money + (money*0.1)
    return money


deposit = float(input("Enter amount of money for deposit: "))
duration = int(input("Enter period of time in years for deposit: "))
total = depos(deposit, duration)
print(total)