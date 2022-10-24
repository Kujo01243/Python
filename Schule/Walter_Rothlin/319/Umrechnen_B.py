#!/usr/bin/python3
from function_libary.Josias_function_libary import *

# =============
# Hauptprogramm
# =============
doLoop = True
while doLoop:
    print("  \nUmrechnungen")
    print("  ====================")
    print("  1: Grad in Bogenmass")  # rad  = grad*pi/180
    print("  2: Bogenmass in Grad")  # grad = rad*180/pi
    print()
    print("  3: Fahrenheit in Celsius")  # 32F -> 0°C    100F -> 38.8°C     °C = (°F - 32) / 1.8
    print("  4: Celsius in Fahrenheit")  # 32F -> 0°C    100F -> 38.8°C     °F = (°C * 1.8) - 32
    print()
    print("  9: Format_String Test")
    print()
    print("  0: Schluss")

    antwort = input("\n  Wähle:")
    if antwort == "1":
        print("Grad --> Bogenmass")
        gradValue = float(input("Grad:"))
        print(f"Grad={gradValue:1.2f}  ==> Rad={grad2Rad(gradValue):1.2f}")
        halt()
    if antwort == "2":
        print("Bogenmass --> Grad")
        radValue = float(input("Rad:"))
        print(f"Rad={radValue:1.2f}  ==> Grad={rad2Grad(radValue):1.2f}")
        halt()
    if antwort == "3":
        print("Fahrenheit in Celsius")
        fahrenheitValue = float(input("Fahrenheit:"))
        print(f"Fahrenheit={fahrenheitValue:1.2f}  ==> Celsius={fahrenheit2Celsius(fahrenheitValue):1.2f}")
        halt()
    if antwort == "4":
        print("Celsius in Fahrenheit")
        celsiusValue = float(input("Celsius:"))
        print(f"Celsius={celsiusValue:1.2f}  ==> Fahrenheit={celsius2Fahrenheit(celsiusValue):1.2f}")
        halt()
    if antwort == "0":
        doLoop = False

print("Ende....Done")