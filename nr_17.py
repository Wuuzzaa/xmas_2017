# Die ersten Lösungen sind in der Aufgabe gegeben
# Jeder Anzahl von Elementen in einer Teilliste wird die Anzahl der Möglichen Kombinationen zugeteilt
# So gibt es bei 4 Elementen in einer Liste 5 zulässige Möglichkeiten
# Um die Lösung von n zu berechnen muss das Ergebnis von n-1 bekannt sein
loesungen = {1: 1,
             2: 1,
             3: 2,
             4: 5}

# Nacheinander die Lösungen von 5 bis 21 berechnen
for i in range(5, 22):
    laenge = i
    zahlen = [x for x in range(1, laenge + 1)]

    def berechne_moeglichkeiten(l, r):
        # Die Anzahl der gesamten Möglichkeiten entspricht der Anzahl der Möglichkeiten der linken Klammer
        #  mal der Anzahl der Möglichkeiten der rechten Klammer
        return loesungen[len(l)] * loesungen[len(r)]

    moeglichkeiten = 0

    # Erzeugt die Elemente der Linken und Rechten Klammer
    for x in range(1, len(zahlen)):
        moeglichkeiten += berechne_moeglichkeiten(zahlen[:x], zahlen[x:])
    loesungen[laenge] = moeglichkeiten

print("Es gibt {} Möglichkeiten 20 nicht triviale Klammerpaare einzufügen".format(loesungen[21]))

