# Autor: Josias Theil
import math


# Konstanten
# ==========
halbBogen = 180

#====================
# functions:
#====================
def halt(prompt="Weiter?"):
    ant = input(prompt)


def isitnumber(number):
    numberloop = True
    while numberloop == True:
        number2 = number
        number2 = number2.replace(".", "", 1)
        number2 = number2.replace("-", "", 1)
        prüfung = number2.isdigit()
        if prüfung == True:
            numberloop = False
        else:
            number = input("Bitte eine ZAHL eingeben!!!: ")
    return float(number)


def grad2rad(grad):
    return grad * 3.1415 / 180

def rad2grad(rad):
    grad = rad * 180 / 3.1415
    print("Ergebnis:", grad)

def fahrenheit2grad(fahrenheit):
    celsius = fahrenheit - 32
    celsius = 5 / 9 * celsius
    print("Ergebnis:", celsius)

def grad2fahrenheit(celsius):
    fahrenheit = celsius * 1.8 + 32
    print("Ergebnis:", fahrenheit)

#=====================
#Hauptprogramm
#============


doLoop = True
while doLoop:

    print("\n\nUmrechnungen")
    print("============")
    print("1: Grad in Bogenmass")
    print("2: Bogenmass in Grad")
    print()
    print("3: Fahrenheit in Grad")
    print("4: Grad in Fahrenheit")
    print()
    print("5 Sin(x) deg")
    print("")
    print("0: Schluss")
    print("============")

    antwort = input("\nWähle: ")

    if antwort == "1":
        print("Grad --> Bogenmass")
        rad2grad(isitnumber(input("Grad: ")))
        halt()

    elif antwort == "2":
        print("Bogenmass --> Grad")
        rad2grad(isitnumber(input("Bogenmass: ")))
        halt()

    elif antwort == "3":
        print("Fahrenheit --> Grad Celsius")
        fahrenheit2grad(isitnumber(input("Fahrenheit: ")))
        halt()

    elif antwort == "4":
        print("Grad Celsius --> Fahrenheit")
        grad2fahrenheit(isitnumber(input("Grad Celsius: ")))
        halt()

    elif antwort == "5":
        print("")
        doLoop = True
        while doloop:
            if eingabe == "platzhalter":

                doLoop = False
            elif eingabe == "platzhalter":

                doLoop = False
            else:
                print("Bitte gültige Eingabe machen: ")
                input(eingabe)
        halt()

    elif antwort == "0":
        print("Programm wird beendet!!!\nTschüss!!!")
        doLoop = False

    else:
        print("ungültige Eingabe bitte gültige Eingabe machen!\n\n")
        halt()
































