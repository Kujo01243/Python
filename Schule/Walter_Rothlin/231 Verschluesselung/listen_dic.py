print("listen and dict (JSON=)")

# Listen in Python
nameListe = ['Walti', "Felix", "Hans", 'Lukas']
print(nameListe)
print(nameListe[1], len(nameListe))
for aName in nameListe:
    print("aName:", aName[0:3], aName[-1], len(aName), aName[-3:])

nameListe.sort()
print(nameListe)

# Dictonaries in Python
capitols = {
    "Schweiz" : "Bern",
    "Deutschland" : "Berlin",
    "Oesterreich" : "Wien",
    "Italien" : "Rom",
    "Frankreich" : "Paris",
    "Liechtenstein" : "Vaduz"
}


print(capitols)
print(capitols["Schweiz"])
for aKey in capitols:
    print(aKey,"-->", capitols[aKey])

# combinations of dicts and lists
countries = {
    "Schweiz": {"Capitol": "Bern", "Population" : "8Mio", "Währung" : "Franken und Rappen"}
}
print(countries)
print(countries["Schweiz"]["Capitol"])
print(countries["Schweiz"]["Population"])
print(countries["Schweiz"]["Währung"])