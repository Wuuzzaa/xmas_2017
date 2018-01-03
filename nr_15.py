def rentiere_erstellen(n):
    rentiere = []
    for i in range(1,n+1):
        rentiere.append(i)
    return rentiere

k = 1 # Schrittzahl bei der ein Rentier nicht putzen muss (gelöscht wird)
while True:
    rentiere = rentiere_erstellen(1234)
    k += 1
    j = 0  # aktueller Schritt
    i = -1  # laufvariable
    while len(rentiere) > 1:
        j += 1
        i += 1

        # Rentiere löschen
        if j == k:
            rentiere.pop(i)
            j = 0
            i -= 1  # i um eins zurücksetzen, da ein wert aus der liste entfernt wird
            #print(rentiere)

        # Laufvariable zurücksetzen
        if i == len(rentiere)-1:
            i = -1

    # Lösung gefunden
    if rentiere[0] == 1:
        break

print("Bei Schritten von {} muss Rudolph putzen".format(k))














