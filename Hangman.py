import random


from contry_and_capital_list import countries_and_capitals
from ascii import HANGMANPICS

def hangmanci(city):
    for i in city:
        if i == ' ':
            hidden1.append(' ')
        else:
            hidden1.append('-')
    print(''.join(hidden1))
    return city, city.count(' ')

def hangmancu(country):
    for i in country:
        if i == ' ':
            hidden2.append(' ')
        else:
            hidden2.append('-')
    print(''.join(hidden2))
    return country, country.count(' ')

fut = True
hidden1 = []
hidden2 = []
orszag=[]
capital=[]

while fut:
    for i in countries_and_capitals():
        x, y = i.strip().split("|")
        x=x.lstrip()
        y=y.lstrip()
        orszag.append(x)
        capital.append(y)
    ran_country=random.randint(0, (len(orszag)))
    ran_capital=random.randint(0, (len(capital)))


    city = capital[ran_capital]
    country = orszag[ran_country]

    print("[1] Ország")
    print("[2] Főváros")
    print("[ENTER] Kilépés")
    choice = input()

    if choice == '1':
        hangmancu(country)
        country.clear()
    elif choice == '2':
        hangmanci(city)
    elif choice == '':
        Fut = False

hibapont = 0
print('Köszönjük a játékot')