file_path = "data/random.txt"

file = open(file_path)
zahlen = file.readlines()
zahlen.sort()
anzahl_zeilen = len(zahlen)
kleinste_differenz = 99999999999999999999999

for i in range(anzahl_zeilen -1):
    x = int(zahlen[i])
    y = int(zahlen[i + 1])
    delta = y - x

    if kleinste_differenz > delta > 0:
        kleinste_differenz = delta

print("Kleinste Differenz: {}".format(kleinste_differenz))
