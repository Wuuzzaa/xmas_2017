brueche = [(0, 1), (1, 0)]

# so lange brueche erzeugen, bis 37/100 vorhanden ist
while (37, 100) not in brueche:
    temp_brueche = brueche
    for i in range(len(brueche)-1):
        # Nur in ungeraden i einfügen
        if i % 2 == 0:
            temp_brueche.insert(i+1, (brueche[i][0] + brueche[i+1][0], brueche[i][1] + brueche[i+1][1]))
            i += 1
    print(brueche)
    brueche = temp_brueche


# 0,1 und 1,1 löschen
# binary search
