file_path = "data/random.txt"

file = open(file_path)
zeilen = file.readlines()
menge_unterschiedlicher_endungen = set()
gesuchte_zeile = 0

for zeile in zeilen:
    menge_unterschiedlicher_endungen.add(abs(int(zeile)) % 1000)
    gesuchte_zeile += 1

    if len(menge_unterschiedlicher_endungen) == 1000:
        print("Alle Endungen [0-999] sind ab Zeile {} min. einmal vorgekommen".format(gesuchte_zeile))
        break
