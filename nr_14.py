def neue_zeile_berechnen(alte_zeile, istGeradeZeile):
    neue_zeile = []

    # alte_zeile am Anfang und Ende eine 0 hinzufügen
    alte_zeile.append(0)
    alte_zeile.insert(0, 0)

    # Gerade Reihe - rechts -> links
    if istGeradeZeile:
        for i in range(len(alte_zeile)-1, -1, -1):
            neue_zeile.append(sum(alte_zeile[i:len(alte_zeile)-1]))
        neue_zeile.reverse()

    # Ungerade Reihe - links -> rechts # geht
    else:
        for i in range(len(alte_zeile)):
            neue_zeile.append(sum(alte_zeile[:i]))

    # Jede 2 Zahl nullsetzen
    for i in range(1, len(neue_zeile), 2):
        neue_zeile[i] = 0
    return neue_zeile

alte_zeile = [0,0,5,0,10,0,14,0,16,0,16] # Zeile 5
istGeradeZeile = True   # True, da erste berechnete Zeile 6 ist
for i in range(10):
    neue_zeile = neue_zeile_berechnen(alte_zeile, istGeradeZeile)
    alte_zeile = neue_zeile
    istGeradeZeile = not istGeradeZeile

print("In der 15. Zeile steht ganz rechts die Zahl: {}".format(alte_zeile[-1]))
