brueche = [(0, 1), (1, 0)]

# so lange brueche erzeugen, bis 37/100 vorhanden ist
while (37, 100) not in brueche:
    neue_brueche = []
    # Neue Brüche erzeugen
    for i in range(len(brueche)-1):
        neue_brueche.append((brueche[i][0] + brueche[i+1][0], brueche[i][1] + brueche[i+1][1]))
    #print(neue_brueche)
    # Neue Brüche mit alten mergen
    alte_brueche = brueche
    brueche = [] # leeren um append einfach zu nutzen
    while neue_brueche:
        # alten Bruch hinzufügen
        brueche.append(alte_brueche.pop())
        # neuen Bruch hinzufügen
        brueche.append(neue_brueche.pop())
    # letzen alten Bruch hinzufügen
    brueche.append(alte_brueche.pop())

brueche.reverse()

# 0,1 und 1,0 löschen
brueche.remove((0, 1))
brueche.remove((1, 0))

# binary search
wert_gesucht = 37/100
wert_mitte = wert_mitte = brueche[int(len(brueche)/2)][0] / brueche[int(len(brueche)/2)][1]
loesung = ""
while wert_mitte != wert_gesucht:
    # Gesuchter Wert ist kleiner als Mitte -> L
    if wert_gesucht <= wert_mitte:
        loesung += "L"
        brueche = brueche[0:int(len(brueche)/2)]
    # Gesuchter Wert ist größer als Mitte -> R
    else:
        loesung += "R"
        brueche = brueche[int(len(brueche)/2):]

    wert_mitte = wert_mitte = brueche[int(len(brueche) / 2)][0] / brueche[int(len(brueche) / 2)][1]

print("Lösung: {}".format(loesung))