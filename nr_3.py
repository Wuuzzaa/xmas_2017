file_path = "C:\\Users\\Jonas\Desktop\\random\\random.txt"

file = open(file_path)
inhalt = file.readlines()
anzahl_zeilen = len(inhalt)
kleinste_differenz = 99999999999999999999999

# alle positiven zahlen löschen


for i in range(anzahl_zeilen):
    x = inhalt[i]

    for k in range(anzahl_zeilen):
        if i == k:
            continue

        y = inhalt[k]

        #if (int(x) - int(y)) < kleinste_differenz:
            #kleinste_differenz = int(x) - int(y)

        if int(x) > int(y):
            if (int(x) - int(y)) < kleinste_differenz:
                kleinste_differenz = int(x) - int(y)

        else:
            if (int(y) - int(x)) < kleinste_differenz:
                kleinste_differenz = int(y) - int(x)


    if i % 10000 == 0:
        print(str(i) + ": Durchlauf")
        print("Kleinste Differenz = " + str(kleinste_differenz))

print("Kleinste Differenz = " + str(kleinste_differenz))

