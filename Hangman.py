import random


from contry_and_capital_list import countries_and_capitals


country=[]
capital=[]

for i in countries_and_capitals():
    x, y = i.strip().split("|")
    x=x.replace(" ", "")
    y=y.replace(" ", "")
    country.append(x)
    capital.append(y)
ran_country=random.randint(0, (len(country)))
ran_capital=random.randint(0, (len(capital)))
print(country[ran_country])
print(capital[ran_capital])








