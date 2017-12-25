file_path = "data/random.txt"

file = open(file_path)
zeilen = file.readlines()
laengste_teilfolge = 0


def ist_nachfolger_groesser(index):
    return int(zeilen[index + 1]) > int(zeilen[index])

for i in range(len(zeilen)-1):
    aktuelle_teilfolge = 1
    while ist_nachfolger_groesser(i):
        aktuelle_teilfolge += 1
        i += 1

    if aktuelle_teilfolge > laengste_teilfolge:
        laengste_teilfolge = aktuelle_teilfolge

print("Längste echt aufsteigende Teilfolge ist {} lang".format(laengste_teilfolge))