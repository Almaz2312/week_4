"""
Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12), и возвращающую время года, которому этот месяц принадлежит (зима, весна, лето или осень).
"""

month = int(input("Month No. (1-12): "))
def season(x):
    if x >= 1 and x <= 2:
        print("Winter")
    elif x == 12:
        print("Winter")
    elif x >= 3 and x <= 5:
        print("Spring")
    elif x >= 6 and x <= 8:
        print("Summer")
    elif x >= 9 and x <= 11:
        print("Autumn")
    else:
        print("Wrong number")


season(month)