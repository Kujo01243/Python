#-----------------------------------------------------------------------
# Name: Shiffre.py
# Discription: Crypto Maschine in Python
# Autor: Josias Theil
# Version: 05.11.2021
#
#
#
#
#
#
#
#----------------------------------------------------------------------
def shift(sChar, offset):
    return  chr(ord(sChar) + offset)

def encrypt(plainText, key):
    return "Verschluesselter Text"


plainText = '''Hallo BZU'''
key = 5

# print("plaintext:", plainText)
# for singleChar in plainText:
#     print(singleChar, ord(singleChar), ord(singleChar) + key, chr(ord(singleChar) + key), shift(shift(singleChar, key), -key))

print("plaintext: ", plainText)
print("Chiffrat:"encrypt(plainText, key))