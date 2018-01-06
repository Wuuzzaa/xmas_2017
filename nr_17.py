laenge = 3
zahlen = [x for x in range(1, laenge + 1)]


def berechne_klammerpaare(linke_klammer, rechte_klammer):
    #print("linke klammer {}".format(linke_klammer))
    #print("rechte klammer {}".format(rechte_klammer))
    global ergebnisse

    if linke_klammer and rechte_klammer:
        ergebnisse += 1

    if len(linke_klammer) > 2:
        #return berechne_klammerpaare(linke_klammer[1:], rechte_klammer)
        for x in range(1, len(linke_klammer) ):
            return berechne_klammerpaare(linke_klammer[:x], linke_klammer[x:])

    if len(rechte_klammer) > 2:
        #return berechne_klammerpaare(linke_klammer, rechte_klammer[1:])
        for x in range(1, len(rechte_klammer) ):
            return berechne_klammerpaare(rechte_klammer[:x], rechte_klammer[x:])

global ergebnisse
ergebnisse = 0

for x in range(1, len(zahlen)):
    print("linke klammer {}".format(zahlen[:x]))
    print("rechte klammer {}".format(zahlen[x:]))
    berechne_klammerpaare(zahlen[:x], zahlen[x:])

print(ergebnisse)