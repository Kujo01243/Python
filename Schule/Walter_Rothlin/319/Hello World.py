# !/usr/bin/python3
#script von Josias Theil

import sys
import os

print ("hello world")
print ("Hello", "World", "!!!")
print ("Hello", "World", "!!!", sep="_") # mit sep wird entschieden, was zwischen den einzelnen Wörtern steht.
print ("Hello", "\nWorld", "\n!!!")
print ("Radius")


#-------------------------------------------------------------------------------------------------------------------
a = 1.5612
b = 45.2125
c = 10023.345
d = 100.05


print (f"|{a:+10.2f}|",f"{b:+10.2f}|",f"{c:+10.2f}|",f"{d:+10.2f}|")
print (f"|{a:10}|",f"{b:10}|",f"{c:10}|",f"{d:10}|")
print (f"|{a:10}|",f"{b:10}|",f"{c:10}|",f"{d:10}|")
print (f"|{a:010}|",f"{b:010}|",f"{c:010}|",f"{d:010}|")
print (f"|{a:10}|",f"{b:10}|",f"{c:10}|",f"{d:10}|")

#--------------------------------------------------------------------------------------------------------------------
#input
string = input("input something: ")
pri