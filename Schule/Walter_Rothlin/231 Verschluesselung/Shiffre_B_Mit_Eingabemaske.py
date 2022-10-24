# ------------------------------------------------------------------
# Name: SymCrypterEncrypterFct.py
#
# Description: Crypto Maschine in Python
#
# Autor: Walter Rothlin
#
# History:
# 05-Nov-2021   Walter Rothlin      Initial Version
# 11-Nov-2021   Walter Rothlin      Implemented Ringbuffer Shifter, encrypter, decrypter
# ------------------------------------------------------------------

def shifter(sChr, sh):
    retVal = chr(ord(sChr) + sh)
    return retVal

# shifter using ringbuffer
def shiftChr(aChar, shift):
    return chr(((ord(aChar) - ord(' ') + shift) % (ord('~') - ord(' ') + 1)) + ord(' '))

def encrypt(klartext, key):
    keyIndex = 0
    geheimtext = ""
    for aChar in klartext:
        if (aChar >= "") and (aChar <= "~"):
            aKeyChr = key[keyIndex]
            shifter = ord(aKeyChr)
            aSecretChr = shiftChr(aChar, shifter)
            # print(aChar, " (Rigth-Shift: ord(", aKeyChr, ") ", shifter, ") --> ", aSecretChr, sep="")
            keyIndex = keyIndex + 1
            if (keyIndex >= len(key)):
                keyIndex = 0
            geheimtext = geheimtext + aSecretChr
    return geheimtext

def decrypt(geheimtext, key):
  keyIndex = 0
  encryptedtext = ""
  for aChar in geheimtext:
     if (aChar >= "") and (aChar <= "~"):
        aKeyChr = key[keyIndex]
        shifter = ord(aKeyChr)
        decryptedChar = shiftChr(aChar, -shifter)
        # print(aChar, " (Left-Shift:        ", -shifter, ") --> ", decryptedChar, sep="", end="\n\n")
        keyIndex = keyIndex + 1
        if (keyIndex >= len(key)):
           keyIndex = 0
        encryptedtext = encryptedtext + decryptedChar
  return encryptedtext


#eingabemaske
x = 0
while x == 0:                                                           #Solange x = 0, bleibt es in dieser Schleife
    print("=======================================")
    print("Verchluesseln 1")
    print("Entschluesseln 2")
    print("Zum beenden 3")
    y = float(input())
    print("=======================================")
    while  y > 3:
        print("Bitte korrekten Wert eingeben")
        y = -1
    while y == 3:
        print("Auf wiedersehen!")
        x = 1                                                           #Hier wird x auf 1 gesetzt, damit es das Script verlässt.
        y = -1                                                          # Hier wird y auf 5 gesetzt, damit es die Unterschleife verlässt.
    while y == 1:
        klartext = input("Klartext:")
        key = input("key:")
        laenge = len(key)
        if laenge < 3:                                                  #Hier wird überprüft, ob der Key kürzer als 3 Zeichen ist. Wenn ja, wird der User informiert.
            print("DER KEY IST KÜRZER ALS 3 ZEICHEN, WAS DEN KEY UNSICHER MACHT!!!")
            chiffrat = encrypt(klartext, key)
            print("Klartext:", klartext, "   Key:", key)
            print("Chiffrat:", chiffrat)
            print()
            y = -1
        else:
            chiffrat = encrypt(klartext, key)
            print("Klartext:", klartext, "   Key:", key)
            print("Chiffrat:", chiffrat)
            print()
            y = -1                                                          #Hier wird y auf 5 gesetzt, damit es die Unterschleife verlässt.
    while y == 2:
        chiffrat = input("Chiffrat:")
        key = input("Key:")
        dechiffrat = decrypt(chiffrat, key)
        print("Chiffrat:", chiffrat, "   Key:", key)
        print("Klartext  :", dechiffrat)
        print()
        y = -1                                                             #Hier wird y auf 5 gesetzt, damit es die Unterschleife verlässt.


