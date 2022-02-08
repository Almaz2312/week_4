"""
Банкомат
Напишите код банкомата, который принимает цифру, выдает деньги с номиналом 5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 3, 1.
"""

change = [2000, 1000, 500, 200, 100, 50, 20, 10, 5, 3, 1, 5000]
nums = int(input("Enter number: "))
def withdraw(total):
    change.sort(reverse=True)
    for banknote in change:
        while total >= banknote:
            total -= banknote
            print(f'Выдано: {banknote}')


withdraw(nums)
