pi = 3.142


def kreis():
    durchmesser1=100
    durchmesser2=10
    grokre = durchmesser1/2*durchmesser1/2*pi
    kleikre = durchmesser2/2*durchmesser2/2*pi
    result = (grokre-kleikre)
    return result
print("Resultat: ", kreis(), "mm2")

def dreieck():
    höhe = 50
    basis = 80
    flächedreieck = (höhe*basis/2)
    quadratseite = 5
    quadratfläche = (quadratseite*quadratseite)
    result = (flächedreieck-quadratfläche)
    return result
print("Resultat: ", dreieck(), "mm2")


