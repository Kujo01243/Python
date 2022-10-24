###########################################################################
'''
Autor: Josias Theil
'''
###########################################################################
#imports:
import math
###########################################################################
#Beschreibung_copy
'''
###########################################################################
#"Titel"
#Variabeln input:
#Variabel - Variabelbeschreibung

#return:
#Was als Rückgabewert kommt
'''
#############################################################################
#Grad to rad
#Variabeln input:
#grad - Grad Celsius

#return:
#rad

def grad2Rad(grad):
    halbBogen = 180
    return math.pi * grad / halbBogen
###########################################################################
#rad to grad
#Variabeln input:
#rad - eingabe rad

#return:
#grad

def rad2Grad(rad):
    halbBogen = 180
    return halbBogen * rad / math.pi

###########################################################################
#stop bis enter
#Variabeln input:
# -

#return:
# -

def halt(prompt="Weiter?"):
    ant = input(prompt)


###########################################################################
#Fahrenheit in Grad Celsius
#Variabeln input:
#fahrenheit - Fahrenheit zur Eingabe

#return:
#Grad Ceisius

def fahrenheit2Celsius(fahrenheit):
    return (fahrenheit - 32) / 1.8


###########################################################################
#Grad Celsius zu Fahrenheit
#Variabeln input:
#celsius - Grad Celsius

#return:
#fahrenheit

def celsius2Fahrenheit(celsius):
    return (celsius * 1.8) + 32

###########################################################################
#Passwortüberpfüfung
#Varbabeln:
#password - Passwort was übergeben wird
#longerThen - Passwort muss länger als sein (standard=6)
#minCountofFigures - wie viele Zahlen mindestens enthalten sein müssen (standard=1)
#showErrorMsg - sollen Fehlermeldungen ausgegeben werden (standard=False)

#Return:
#True of False

def is_valid_passwort(password, longerThen=6, minCountOfFigures=1, showErrorMsg=False):
    if len(password) >= longerThen + 1:
        if count_figures_in_string(password) >= minCountOfFigures:
            return True
        else:
            if showErrorMsg:
                print(password, "has no figures in it!")
        return False
    else:
        if showErrorMsg:
            print(password, "too short!")
        return False

###########################################################################
#Nach Anzahl zahlen abfragebn
#Variabeln:
#aString - der Text

#Return:
#Anzahl zahlen in einem String

def count_figures_in_string(aString):
    count = 0
    for aChar in aString:
        if "0" <= aChar <= "9":
            count = count + 1
    return count

###########################################################################
#Abfrage ob Primzahl oder nicht
#Variabeln:
#aZahl - eine Zahl zum übergeben

#Return:
#True of False

def isPrimzahl(aZahl):
    isPrim = False
    if aZahl == 1 or aZahl == 2:
        isPrim = True
    else:
        isPrim = True
        obergrenze = int(aZahl / 2) + 1
        for i in range(2, obergrenze + 1):
            if (aZahl % i) == 0:  # Kein Rest
                isPrim = False
    return isPrim

###########################################################################
#Nächst grössere Primzahl ausgeben
#Variabeln:
#aZahl - eine zahl zum übergeben

#Return:
#nächst grössere Primzahl


def getNextPrimzahl(aZahl):
    while True:
        aZahl = aZahl + 1
        if isPrimzahl(aZahl):
            return aZahl

###########################################################################
#Nächst kleinere Primzahl
#Variabeln:
#aZahl - einen Zahl zum übergeben

#Ausgabe:
#nächst kleinere Primzahl

def getPrevPrimzahl(aZahl):
    while True:
        if aZahl <= 1:
            print('Es gibt keine kleineren Primzahlen mehr! Es wurde einfach 1 als kleinste Primzahl zurückgegeben!')
            return 1
        aZahl = aZahl - 1
        if isPrimzahl(aZahl):
            return aZahl


###########################################################################
#Liste von Primzahlen von bis mit auswählbarem getrennt:
#Variabeln:
#start - start von Primzahlen
#end - ende von Primzahlen
#sep - Trennungszeichen

#Ausgabe:
#entweder alle Primzahlen zwischen start und end. Wenn end grösser als start oder es keine Primzahlen in der Range gibt:
#Meldung "Es wurden keine Primzahlen gefunden!"

def getPrimezahlenListe(start, end, sep=";"):
    list = ""
    while True:
        if start <= end:
            if isPrimzahl(start):
                start2 = (str(start) + str(sep))
                list = (str(list) + str(start2))
            start = getNextPrimzahl(start)
        else:
            if len(list) < 1:
                return print("Es wurden keine Primzahlen gefunden!")
            else:
                return list[:-1]

###########################################################################
#Ausgabe von Primzahlen zwischen start und end
#Variabeln:
#start - start von Primzahlen
#end - ende von Primzahlen

#Ausgabe:
#Alle Primzahlen als print, die zwischen start und end liegen in einer Liste


def getPrimezahlenAsListe(start, end):
    returnwert0 = ""
    liste = []
    while True:
        if start <= end:
            if isPrimzahl(start):
                liste.append(start)
            start = getNextPrimzahl(start)
        else:
            return liste


###########################################################################
#Primfaktorzerlegung
#Variabeln:
#zahl - Zahl, die zerlegt werden soll
#sep - Trennzeichen

#Ausgabe:
#Primfaktorzerlegung von zahl


def getPrimfactors(zahl, sep = "*"):
    list = ""
    ersterteiler = 2
    while ersterteiler < (zahl + 1):
        ganzzahlchecker = (zahl/ersterteiler)
        if ganzzahlchecker == int(ganzzahlchecker):
            ersterteiler2 = (str(ersterteiler) + str(sep))
            list = (str(list) + str(ersterteiler2))
            zahl = (zahl/ersterteiler)
        else:
            ersterteiler = getNextPrimzahl(ersterteiler)
    return list[:-1]
###########################################################################
#Primfaktorzerlegung als Print
#Variabeln:
#zahl - Zahl, die zerlegt werden soll

#Ausgabe:
#Primfaktorzerlegung von zahl als jeweis einzelner Print

def getPrimfactorsAsListe(zahl):
    returnwert0 = ""
    ersterteiler = 2
    while ersterteiler < (zahl + 1):
        ganzzahlchecker = (zahl / ersterteiler)
        if ganzzahlchecker == int(ganzzahlchecker):
            print(ersterteiler)
            zahl = (zahl / ersterteiler)
        else:
            ersterteiler = getNextPrimzahl(ersterteiler)
    return returnwert0

###########################################################################


