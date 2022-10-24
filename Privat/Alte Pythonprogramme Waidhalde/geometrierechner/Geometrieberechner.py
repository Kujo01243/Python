print('willkommen zu meinen Berechnungen')
from math import*
x = 0
while x == 0:
    print ('\nbitte Zahl auswählen:')
    print ('Pyramiedenvolumen drücke:                                              "1"')
    print ('Kreisumfang drücke:                                                    "2"')
    print ('Kreisfläche drücke:                                                    "3"')
    print ('Fläche eines regelmässigen Sechseck drücke:                            "4"')
    print ('Volumen einer Kugel drücke:                                            "5"')
    print ('von Volumen Kugel auf radius und durchmesser drücke:                   "6"')
    print ('die Fläche eines gleichseitigen dreiecks drücke:                       "7"')
    print ('für die Formeln bitte die 100 eingeben.')
    x = float(input(':'))
    if x == 0:
        print('\nbitte eine Zahl wählen, welche den Anforderungen entschpricht')
    if x == 100:
        print('Pyramiedenvolumen: V=(a**2*h)/3\nKreisumfang: U=r*2*pi\nKreisfläche: A=r**2*pi\nFläche eines reg. sechsecks: A=(a**2*(sqrt)3)/4*6\nVolumen einer Kugel: V=4/3*pi*r**3')
        print('von Volumen einer Kugel auf radius: R=((V/pi)(3/4))**1/3\ngleichseitiges Dreieck: A=(a**2*(sqrt)3)/4')
        x = 0

        
    while x == 7:
        print('\ngleichseitiges dreieck')
        a = float (input("Seitenlänge: "))
        b = (a/2)
        c = (a**2-b**2)
        h = (sqrt(c))
        d = (h*b)
        print('\ndie Fläche beträgt:',d,'cm2')
        print('\ndie Höhe h beträgt:',h,'cm')
        x = 0
    while x == 6:
        print('\nden Radius aus dem Volumen einer Kugel')
        v = float(input('Volumen: '))
        t = (1/3)
        u = (v*3)
        i = (pi*4)
        o = (u/i)
        r = (o**t)
        d = (r*2)
        print('\nder Radius beträgt:',r,'cm')
        print('\nder Durchmesser beträgt:',d,'cm')
        x = 0  
    while x == 5:
        print('\nVolumen einer Kugel')
        r = float(input('Radius: '))
        v = (4/3*pi*r**3)
        print('\ndas Volumen beträgt:',v,'cm3')
        x = 0
    while x == 4:
        print('\nFläche eines regelmässigen sechseck')
        a = float (input("Seitenlänge: "))
        b = (a/2)
        c = (a**2-b**2)
        d = (sqrt(c)*b)
        e = (d*6)
        print('\ndie Fläche beträgt: ',e,"cm2")
        x = 0
    while x == 3:
        print('\ndie Fläche eines Kreises')
        r = float (input("radius: "))
        f = (r**2*pi)
        print ("\ndie Fläche beträgt: ",f,"cm2")
        x = 0
    while x == 2:
        print ('\nder Umfang eines Kreises')
        r = float (input("radius: "))
        f = (r*2*pi)
        print ("\nder Umfang beträgt: ",f,"cm")
        x = 0
    while x == 1:
        print('\nPyrmaiedenvolumen')
        l = float (input("Länge der Grundfläche: "))
        b = float (input("Breite der Grundfläche: "))
        h = float (input("höhe der Grundfläche: "))
        g = (b*l)
        v = (1/3*g*h)
        print ("\ndas Volumen beträgt: ",v,"cm3")
        x = 0
    if x > 0:
        print('\nbitte eine Zahl wählen, welche den Anforderungen entschpricht')
        x = 0