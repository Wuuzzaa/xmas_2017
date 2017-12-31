file_path = "data/teilsumme.txt"

file = open(file_path)
zeilen = file.readlines()
groesste_teilsumme = 0

for i in range(len(zeilen)):
    # Negative Startzahl
    if int(zeilen[i]) < 0:
        continue
    # Positive Startzahl
    aktuelle_teilsumme = int(zeilen[i])

    if aktuelle_teilsumme > groesste_teilsumme:
        groesste_teilsumme = aktuelle_teilsumme

    # von i-ter Stelle bis ende durchlaufen
    for k in range(i+1, len(zeilen)):
        aktuelle_teilsumme += int(zeilen[k])

        if aktuelle_teilsumme > groesste_teilsumme:
            groesste_teilsumme = aktuelle_teilsumme


print("Groesste Teilsumme ist {} ".format(groesste_teilsumme))