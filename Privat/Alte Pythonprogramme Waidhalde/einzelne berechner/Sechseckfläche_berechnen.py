#regelm. Sechseck berechnen


from math import*
a = float (input("Seitenlänge: "))
b = (a/2)
c = (a**2-b**2)
d = (sqrt(c)*b)
e = (d*6)
print ("die fläche beträgt: ",e)
