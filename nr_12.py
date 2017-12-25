from random import choice

aexte_a = 1
aexte_b = 1
aexte_c = 0
aexte_d = 0
aexte_e = 0


def simulation():
    runden = 0

    global aexte_a
    global aexte_b
    global aexte_c
    global aexte_d
    global aexte_e

    aexte_a = 1
    aexte_b = 1
    aexte_c = 0
    aexte_d = 0
    aexte_e = 0

    while aexte_a < 2 and aexte_b < 2 and aexte_c < 2 and aexte_d < 2 and aexte_e < 2:
        #print(axtwerfer_bestimmen()[0], axtwerfer_bestimmen()[1])
        axtwerfer_1, axtwerfer_2 = axtwerfer_bestimmen()
        werfen(axtwerfer_1, axtwerfer_2)
        runden += 1

    return runden


def axtwerfer_bestimmen():
    global aexte_a
    global aexte_b
    global aexte_c
    global aexte_d
    global aexte_e

    axtwerfer_1 = ""
    axtwerfer_2 = ""

    if aexte_a == 1:
        axtwerfer_1 = "a"

    if aexte_b == 1:
        if axtwerfer_1 == "":
            axtwerfer_1 = "b"
        else:
            axtwerfer_2 = "b"

    if aexte_c == 1:
        if axtwerfer_1 == "":
            axtwerfer_1 = "c"
        else:
            axtwerfer_2 = "c"

    if aexte_d == 1:
        if axtwerfer_1 == "":
            axtwerfer_1 = "d"
        else:
            axtwerfer_2 = "d"

    if aexte_e == 1:
        if axtwerfer_1 == "":
            axtwerfer_1 = "e"
        else:
            axtwerfer_2 = "e"

    return axtwerfer_1, axtwerfer_2


def werfen(axtwerfer_1, axtwerfer_2):
    global aexte_a
    global aexte_b
    global aexte_c
    global aexte_d
    global aexte_e

    # A hat Axt
    if axtwerfer_1 == "a" or axtwerfer_2 == "a":
        ziel = choice(["e", "b"])

        # Axt hinzufügen
        if ziel == "e":
            aexte_e += 1
        else:
            aexte_b += 1

        # Axt entfernen
        aexte_a -= 1

    # B hat Axt
    if axtwerfer_1 == "b" or axtwerfer_2 == "b":
        ziel = choice(["a", "c"])

        # Axt hinzufügen
        if ziel == "a":
            aexte_a += 1
        else:
            aexte_c += 1

        # Axt entfernen
        aexte_b -= 1

    # C hat Axt
    if axtwerfer_1 == "c" or axtwerfer_2 == "c":
        ziel = choice(["b", "d"])

        # Axt hinzufügen
        if ziel == "b":
            aexte_b += 1
        else:
            aexte_d += 1

        # Axt entfernen
        aexte_c -= 1

    # D hat Axt
    if axtwerfer_1 == "d" or axtwerfer_2 == "d":
        ziel = choice(["c", "e"])

        # Axt hinzufügen
        if ziel == "c":
            aexte_c += 1
        else:
            aexte_e += 1

        # Axt entfernen
        aexte_d -= 1

    # E hat Axt
    if axtwerfer_1 == "e" or axtwerfer_2 == "e":
        ziel = choice(["d", "a"])

        # Axt hinzufügen
        if ziel == "d":
            aexte_d += 1
        else:
            aexte_a += 1

        # Axt entfernen
        aexte_e -= 1


runden_liste = []
for i in range(100000000):
    runden_liste.append(simulation())
    if i % 10000 == 0:
        print(str(i) + ": Durchlauf")
        mittelwert = sum(runden_liste) / len(runden_liste)
        print("Mittelwert: " + str(mittelwert))

