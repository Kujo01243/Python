#!/usr/bin/python3

# ------------------------------------------------------------------
# Name  : pythonBasics_12_MetaDataInPicture.py
# Source: https://raw.githubusercontent.com/walter-rothlin/Source-Code/master/Python_WaltisExamples/Code_02_BasicPython/pythonBasics_12_MetaDataInPicture.py
#
# Description: Lädt ein Bild und liesst alle Meta-Tags
#
# Autor: Walter Rothlin
#
# https://pillow.readthedocs.io/en/stable/reference/Image.html#examples    Bildverarbeitung
# http://metapicz.com/#landing  Web-Applikation zum Meta-Tags auslesen
#
# Auf Windows mit File-Explorer Properties --> Details
#
# History:
# 22.4.21   Walter Rothlin      Initial Version
# ------------------------------------------------------------------
from PIL import Image
from time import sleep
x = 0
while x == 0:
    print("Wähle:")
    print("1 für ein einfaches Beispiel")
    print("2 um einen Pfad zu einem individuellen Bild einzugeben")
    waehle = float(input("Wähle: "))
    while waehle == 1:
        img = Image.open("Z:\Pycharm_Projekte\Scripte_Python\Schule\Walter_Rothlin\Verschlüsselung\Bilder\Bildersammlung\Vogt-7.JPG")
        # img = Image.open('Bilder/Bruch_1.jpg')
        # img = Image.open('Bilder/Screenshot.png')

        exif_data = img._getexif()
        print("Meta-Data", exif_data)

        if exif_data is not None:
            for anEntryKey in exif_data:
                print(anEntryKey, "-->", exif_data[anEntryKey])
    #   for angle in range(1, 45, 10):
    #   img.rotate(angle).show()
    #   sleep(0.5)
        waehle = 0
    while waehle == 2:
        pfad = input("Bitte Pfad eingeben: ")
