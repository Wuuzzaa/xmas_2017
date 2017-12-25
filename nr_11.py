from random import choice


def naechster_ausgang():
    return choice(["vorne", "hinten"])


def simulation():
    """
    Gibt die Anzahl an erfolgreichen Spaziergängen zurück
    :return:
    """
    stiefel_vorder = 17
    stiefel_hinter = 19

    spaziergaenge = 0

    ist_gefangen = False
    hat_stiefelan = False

    ausgang = ""
    eingang = ""

    while not ist_gefangen:
        # Höhle verlassen
        ausgang = naechster_ausgang()
        if ausgang == "vorne" and stiefel_vorder > 0:
            stiefel_vorder -= 1
            hat_stiefelan = True

        elif ausgang == "hinten" and stiefel_hinter > 0:
            stiefel_hinter -= 1
            hat_stiefelan = True

        # Night King gefangen?
        if not hat_stiefelan:
            ist_gefangen = True
            #print("Night King schlägt zu")
            #print("{} erfolgreiche Spaziergänge".format(spaziergaenge))
            break

        # Höhle betreten
        eingang = naechster_ausgang()
        if eingang == "vorne" and hat_stiefelan:
            stiefel_vorder += 1
            hat_stiefelan = False

        elif eingang == "hinten" and hat_stiefelan:
            stiefel_hinter += 1
            hat_stiefelan = False

        # Spaziergang erfolgreich
        spaziergaenge += 1
    """
        print("{} Stiefel vorne".format(stiefel_vorder))
        print("{} Stiefel hinten".format(stiefel_hinter))
        if stiefel_hinter + stiefel_vorder != 36:
            raise
    """
    return spaziergaenge


spaziergaenge_liste = []
for i in range(10000000):
    spaziergaenge_liste.append(simulation())
    if i % 10000 == 0:
        print(str(i) + ": Durchlauf")
        mittelwert = sum(spaziergaenge_liste) / len(spaziergaenge_liste)
        print("Mittelwert: " + str(mittelwert))

