#!/usr/bin/python3
from Scripte_Python.function_libary.Josias_function_libary import *

def getDivisors(zahl, sep=";"):
    return False


def getDivisorsAsListe(zahl):
    return False






assert getNextPrimzahl(1) == 2
assert getNextPrimzahl(2) == 3
assert getNextPrimzahl(3) == 5
assert getNextPrimzahl(4) == 5
assert getNextPrimzahl(5) == 7
assert getNextPrimzahl(6) == 7


#assert getPrevPrimzahl(1) == 1
assert getPrevPrimzahl(2) == 1
assert getPrevPrimzahl(3) == 2
assert getPrevPrimzahl(4) == 3
assert getPrevPrimzahl(5) == 3


assert isPrimzahl(1) is True
assert isPrimzahl(2) is True
assert isPrimzahl(3) is True
assert isPrimzahl(4) is False
assert isPrimzahl(5) is True
assert isPrimzahl(6) is False
assert isPrimzahl(7) is True
assert isPrimzahl(8) is False
assert isPrimzahl(9) is False
assert isPrimzahl(10) is False
assert isPrimzahl(11) is True
assert isPrimzahl(12) is False
assert isPrimzahl(13) is True
assert isPrimzahl(14) is False
assert isPrimzahl(15) is False
assert isPrimzahl(16) is False
assert isPrimzahl(17) is True
assert isPrimzahl(18) is False
assert isPrimzahl(19) is True
assert isPrimzahl(20) is False


assert getPrimezahlenListe(1, 100) == "1;2;3;5;7;11;13;17;19;23;29;31;37;41;43;47;53;59;61;67;71;73;79;83;89;97"
print(getPrimezahlenAsListe(1, 100))
assert getPrimfactors(64) == "2*2*2*2*2*2"