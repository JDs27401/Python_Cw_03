import string

#zadanie 1
print("Adam, Anna, Antoni, Andrzej, Aleksander")
print()
#zadanie 2
print("Adam, \nAnna, \nAntoni, \nAndrzej, \nAleksander")
print()
#zadanie 3
def rectangle(a: int, b: int):
    print(b * '*')
    for i in range(a-2):
        print('*' + (b-2) * ' ' + '*')
    print(b * '*')
    print('Obw:', b * 2 + 2 * (a - 2)) #obwód to ilość uzytych gwiazdek
    print('Pole:', a * b)

rectangle(3, 4)
print()
#zadanie 4
price_b = [3.69, 4.5, 3.6, 4.0, 3.99, 3.59]
price_a = [4.5, 5.5, 4.69, 4.99, 4.00]
def showPrices(before, after):
    def avg(list):
        return sum(list)/len(list)
    print("najwyższej cenie po nałożeniu podatku:", min(after))
    print("najniższej cenie biorąc pod uwagę wszystkie ceny (przed i po):", min(before + after))
    print("średniej cenie przed podwyżką cen:", avg(price_b))
    print("średniej cenie po dodaniu nowego podatku:", avg(price_a))

showPrices(price_b, price_a)
print()
# zadanie 5
def printCharacters(list):
    dict = {}
    for name in list:
        dict[name] = len(name)
    print(dict)

printCharacters({"Homelander", "Billy Butcher", "Hughie Campbell", "Black Noir", "Soldier Boy"})
print()
#zadanie 6
def printABS(x):
    print("wartość bezwzględna:", abs(x))

printABS(-12)
print()
#zadanie 7
def printModK(k):
    for i in range(20, 80):
        if i % k == 0:
            print(i, end=", ")

printModK(3)
print()
#zadanie 8
def printModK(k, start, stop):
    for i in range(start, stop):
        if i % k == 0:
            print(i, end=", ")

printModK(5, 10, 20)
print()
#zadanie 10
print()
def comaperNames(a: string, b: string):
    if len(a) > len(b):
        print(a + " jest dłuższe niż" + b)
    elif len(b) > len(a):
        print(b + " jest dłuższe niż " + a)
    else:
        print(a + " i " +  b + " są równe")

comaperNames("Anna", "Zofia")
print()
#zadanie 11
def sumTo100():
    i = 0
    sum = 0
    while i <= 100:
        if i%2!=0:
            sum += i
        i += 1
    print("suma nieparzystych liczb od 1 do 100:", sum)

sumTo100()
print()
#zadanie 12
def printSqr(n: int):
    i = 1
    while i <= n:
        print("kwadra liczby", i, "to:", i**2)
        i += 1

printSqr(5)

# wyniki z teminalu
# Adam, Anna, Antoni, Andrzej, Aleksander
#
# Adam,
# Anna,
# Antoni,
# Andrzej,
# Aleksander
#
# ****
# *  *
# ****
# Obw: 10
# Pole: 12
#
# najwyższej cenie po nałożeniu podatku: 4.0
# najniższej cenie biorąc pod uwagę wszystkie ceny (przed i po): 3.59
# średniej cenie przed podwyżką cen: 3.895
# średniej cenie po dodaniu nowego podatku: 4.736
#
# {'Billy Butcher': 13, 'Homelander': 10, 'Hughie Campbell': 15, 'Soldier Boy': 11, 'Black Noir': 10}
#
# wartość bezwzględna: 12
#
# 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78,
# 10, 15,
#
# Zofia jest dłuższe niż Anna
#
# suma nieparzystych liczb od 1 do 100: 2500
#
# kwadra liczby 1 to: 1
# kwadra liczby 2 to: 4
# kwadra liczby 3 to: 9
# kwadra liczby 4 to: 16
# kwadra liczby 5 to: 25