from random import random

# nr, fass, jahre
rum_liste = []  # beinhaltet rum in produktion
flaschen = []   # beinhaltet rum der fertig produziert ist

# rum fässer befüllen
for i in range(1000000):
    rum_liste.append([i, "A", 0])

# flaschen befüllen
while rum_liste:
    for x in rum_liste:
        # Jahre hochzählen
        x[2] += 1
        # Rum ist in A
        if x[1] == 'A' and random() < 1/3:
            x[1] = 'B'
        # Rum ist in B
        elif x[1] == 'B' and random() < 1/3:
            x[1] = 'C'
        # Rum ist in C
        elif x[1] == 'C' and random() < 1/3:
            x[1] = 'Fertig'
            flaschen.append(x)
    rum_liste = [rum for rum in rum_liste if rum[1] != "Fertig"]

# auswerten
dauer = 0
for x in flaschen:
    dauer += x[2]

mittelwert = dauer / len(flaschen)
print("Mittlere Reifedauer: {}".format(mittelwert))