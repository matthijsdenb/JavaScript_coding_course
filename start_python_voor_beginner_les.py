
# variable verbose
#ikkieszelf = 8
# print(ikkieszelf)

# operator: = assign
# wiskundig: + / * - % // **
# strings = een stuk tekst
# comperative operations:

# variable2 = 7
# variable2 = ikkieszelf
# variable3 = 8+6*ikkieszelf
# print(variable3)

# print(10**4)
#variable4 = 'Maandag'
# print(variable4)

#variable5 = ', Dinsdag'
# print(variable4+variable5)
# print(variable4*5)

#var1 = "Kees"
#var2 = 13

# 'casten': str()
# print(var1+" is mijn zoon en hij is oud: "+str(var2))
# var3 = "15"
# var4 = "17"
# print(int(var3) + int(var4))

# getal1 = input("geef getal 1")
# getal2 = input("geef getal 2")
# print(int(getal1) + int(getal2))

# belangrijke statements: if elif else for
import random
getal5 = 5
if getal5 == 5:
    print("Ja het is vijf")
else:
    print("Nee is het geen vijf")


# operator: = assign
# wiskundig: + / * - % // **
# strings = een stuk tekst, kan gebruikt worden bij * of +
# comperative operations: ==

def wegaanbeginnen():
    x = 5
    if x == 5:
        print("daar gaan we")
        # return  # nu meeten stoppen met de functie
    else:
        print("daar gaan we helemaal niet")
        print("dit is het laatste statement van de functie")


wegaanbeginnen()


def rekenen(param):
    print(str(param)+" + 7 = "+str(param+7))


rekenen(8)
rekenen(12)


def uitrekenen(param, param1):
    print(param + param1)


def uitrekenen(ene, andere):
    if ene > 100:
        print("deze som is te pittig")
        return
    print(ene, "plus", andere, "=", ene+andere)
    return "dit was de som"


uitrekenen(15, 12)
uitrekenen(150, 12)
resultaat = uitrekenen(150, 12)
print(resultaat)

geb3 = 15
geb3 += 5
print(geb3)

# scope
# for
# array

# oefenopdracht
# dranktester 16 18 >18 fris bier alles


def dranktester(leeftijd):
    if leeftijd > 18:
        print("bier")
    else:
        print("geen bier")


dranktester(random.randint(12, 30))
