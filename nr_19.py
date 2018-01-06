# Rechnet ca. 80 Sekunden bis zur Lösung
def berechne_nachbarn(x, y, gueltige_felder):
    #links, rechts, oben , unten
    nachbarn = [(x - 1, y), (x + 1, y), (x, y + 1), (x, y - 1)]

    # ungültige felder löschen
    nachbarn = [feld for feld in nachbarn if feld in gueltige_felder]
    return set(nachbarn) #sets lassen sich schneller durchsuchen


def gueltige_felder_bestimmen():
    min_x, min_y = 0, 0
    max_x, max_y = 5, 5

    quadrat_felder = []

    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            quadrat_felder.append((x, y))
    return set(quadrat_felder) #sets lassen sich schneller durchsuchen


def berechne_wege(start, ziel, bisheriger_weg):
    # Feld wurde zweimal besucht
    if start in bisheriger_weg:
        return
    else:
        bisheriger_weg.append(start)

    # gültiger weg wurde gefunden
    if start == ziel:
        wege.append(bisheriger_weg)
        return

    # Wenn man nicht am Ziel ist probiert man alle möglichen Wege aus
    for feld in nachbarn[start]:
        berechne_wege(feld, ziel, list(bisheriger_weg)) # list cast ist notwendig, da sonst die wege liste bei jedem aufruf weiter geführt wird

# Alle gültigen Felder des Quadrates bestimmen
quadrat_felder = gueltige_felder_bestimmen()

# Nachbarn eines Feldes als dic anlegen
# key feld (x,y)
# values felder (x,y)
global nachbarn
nachbarn = {}

for feld in quadrat_felder:
    nachbarn[feld] = berechne_nachbarn(feld[0], feld[1], quadrat_felder)

global wege
wege = []

berechne_wege((0, 0), (5,5), [])

print("Es gibt insgesamt {} Wege von (0,0) nach (5,5)".format(len(wege)))
