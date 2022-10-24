
aListe = ["walti", "Rothlin"], [8855, 'Wangen'], [123, 567, 12.35]
print(aListe, len(aListe))
print(aListe[2][2])
#aListe.append(True)            #Macht Proobleme
#aListe.append("False")         #Macht Probleme
print(aListe, len(aListe))

for aElement in aListe:
    print(aElement)

i = 1
while i < len(aListe):
    print(i, aListe[i])
    i = i + 1

for i in range(len(aListe)):
    print(i, aListe[i])

print(aListe)
print(aListe[5:-2])

aDict = {
    '8855': {
            "Main": "Wangen",
            "Wyler": "Nuolen"
            },
    '8854': ["Siebnen", "Lachen"]
        }

print(aDict['8854'][1])
print(aDict['8855']['Wyler'])

adressListe = [
    {'Name': 'Rothlin',
     'Vorname': 'Walti',
     'Strasse': 'Peterliwiese 33',
     'PLZ': 8855,
     'Ort': 'Wangen'},
    {'Name': 'Theil',
     'Vorname': 'Josias',
     'Strasse': 'Schürbungert 36',
     'PLZ': 8057,
     'Ort': 'Zürich'}
]
for element in adressListe:
    print(element['Name'])