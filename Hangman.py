import random


from contry_and_capital_list import countries_and_capitals

hidden1 = []
hidden2 = []
country=[]
capital=[]

for i in countries_and_capitals():
    x, y = i.strip().split("|")
    x=x.lstrip()
    y=y.lstrip()
    country.append(x)
    capital.append(y)
ran_country=random.randint(0, (len(country)))
ran_capital=random.randint(0, (len(capital)))


city = capital[ran_capital]
country = country[ran_country]


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


hangmanci(city)
hangmancu(country)







