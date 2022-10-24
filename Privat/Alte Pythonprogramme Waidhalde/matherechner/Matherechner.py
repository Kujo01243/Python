print('einfacher Berechner')
from math import*
entscheider = 0     #hier wird die erste variable (entscheider) definiert.
while entscheider == 0:     #hier wird eine while schleife erstellt, welche aktiv ist solange (entscheider) 0 ist.
    print ('\nwelche Masse brauchst du?:')                                                           #hier wird die anleitung wiedergegeben
    print ('Geschwindigkei:                                       "1"')
    print ('Zeit:                                                 "2"')
    print ('Strecke:                                              "3"')
    x = float(input(':'))                                                                       #hier wird die variable (x) betummen
    if x == 0:                                                                   #wenn man eine falsche zahl eingibt, 'fehler' ausgegeben
        print('\nbitte eine Zahl wählen, welche den Anforderungen entschpricht')

        
    while x == 3:                                  #diese berechnung wird duchgeführt, wenn man die '3' eingibt
        s = float(input('Strecke in km:'))
        t = float(input('Zeit in Stunden:'))
        v = (s/t)
        print('\ndie Geschwindigkeit beträgt:',v,'km/h')
        x = 0                                                               #variable x wird auf 0 gesetzt
        

    while x == 2:                                                   #diese berechnung wird duchgeführt, wenn man die '3' eingibt
        s = float(input('Strecke in km:'))
        v = float(input('Geschwindigkeit in km/h:'))
        t = (s/v)
        print('\ndie Zeit beträgt:',t,'h')
        x = 0                                                                   #variable x wird auf 0 gesetzt

    while x == 1:                                                       #diese berechnung wird duchgeführt, wenn man die '3' eingibt
        t = float(input('Zeit in h:'))
        v = float(input('geschindigkeit in km/h:'))
        s = (t*v)
        print('\nDie Strecke beträgt:',s,'km')
        x = 0                                                          #variable x wird auf 0 gesetzt


    if x > 0:                                                                           #hier wird fehler angezeigt, wenn man die falsche zahl eingibt.
        print('\nbitte eine Zahl wählen, welche den Anforderungen entschpricht')
        x = 0                                                                                   #variable x wird auf 0 gesetzt
