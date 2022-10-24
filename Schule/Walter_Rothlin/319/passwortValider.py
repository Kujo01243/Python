#!/usr/bin/python3

# ------------------------------------------------------------------
# Name  : passwordValiderer.py
# Source: https://raw.githubusercontent.com/walter-rothlin/Source-Code/master/Python_WaltisExamples/Code_00_Pruefung/Intro/passwordValidierer_Aufgabe.py
#
# Description: Checked ob ein Passwort den Regeln entspricht.
#   1) Passwort muss länger als 6 Zeichen lang sein.
#   1a) Passwort muss länger als n Zeichen lang sein (als Argument zu übergeben)
#   2) Passwort muss mindestens eine Ziffer enthalten
#   2a) Passwort muss mindestens n Ziffern enthalten (als Argument zu übergeben)
#
#   Rückgabe: entweder Passwort ist valid: True, Passwort ist ungültig: False
#
# Autor: Walter Rothlin
#
# History:
# 02-Jun-2022   Walter Rothlin      Initial Version
#
# ------------------------------------------------------------------
from function_libary.Josias_function_libary import *

if __name__ == '__main__':
    print("Passwort prüfen:")

    # Diese "asserts" helfen für die Selbstkontrolle, sind alle Asssert Ok - dann funktioniert ihr Prorgramm
    assert is_valid_passwort('muchlonger') is False
    assert is_valid_passwort('12345666') is True
    assert is_valid_passwort('längerse45') is True
    assert is_valid_passwort('kurz') is False
    assert is_valid_passwort('12345') is False
    assert is_valid_passwort('sha5') is False
    assert is_valid_passwort('123456') is False

    assert is_valid_passwort('kurz', 4) is False
    assert is_valid_passwort('12345', 5) is False
    assert is_valid_passwort('sha5', 8) is False

    assert is_valid_passwort('längere45', minCountOfFigures=2) is True
    assert is_valid_passwort('längere45', minCountOfFigures=3) is False

    print("Wenn alles korrekt ist, dann wird diese Zeile ausgegeben !")
    