

# Stapel init
global nordpol
global rovaniemi
global fulda
global s1
global zuege

nordpol = [3, 2, 1]
rovaniemi = []
fulda = []
s1 = 1  # kleinste Scheibe
zuege = []


def bewege_s1():
    global nordpol
    global rovaniemi
    global fulda
    global s1
    global zuege

    # 1 N -> R
    if nordpol and rovaniemi and s1 in nordpol:
        if nordpol[-1] < rovaniemi[-1]:
            rovaniemi.append(nordpol.pop())
            zuege.append(1)
            return

    elif nordpol and not rovaniemi and s1 in nordpol:
        rovaniemi.append(nordpol.pop())
        zuege.append(1)
        return

    # 2 R -> F
    if rovaniemi and fulda and s1 in rovaniemi:
        if rovaniemi[-1] < fulda[-1]:
            fulda.append(rovaniemi.pop())
            zuege.append(2)
            return

    elif rovaniemi and not fulda and s1 in rovaniemi:
        fulda.append(rovaniemi.pop())
        zuege.append(2)
        return

    # 3 F -> R
    if fulda and rovaniemi and s1 in fulda:
        if fulda[-1] < rovaniemi[-1]:
            rovaniemi.append(fulda.pop())
            zuege.append(3)
            return

    elif fulda and not rovaniemi and s1 in fulda:
        rovaniemi.append(fulda.pop())
        zuege.append(3)
        return

    # 4 R -> N
    if rovaniemi and nordpol and s1 in rovaniemi:
        if rovaniemi[-1] < nordpol[-1]:
            nordpol.append(rovaniemi.pop())
            zuege.append(4)
            return

    elif rovaniemi and not nordpol and s1 in rovaniemi:
        nordpol.append(rovaniemi.pop())
        zuege.append(4)
        return


def bewege_nicht_s1():
    global nordpol
    global rovaniemi
    global fulda
    global s1
    global zuege

    # 1 N -> R
    if nordpol and rovaniemi and s1 not in nordpol:
        if nordpol[-1] < rovaniemi[-1]:
            rovaniemi.append(nordpol.pop())
            zuege.append(1)
            return

    elif nordpol and not rovaniemi and s1 not in nordpol:
        rovaniemi.append(nordpol.pop())
        zuege.append(1)
        return

    # 2 R -> F
    if rovaniemi and fulda and s1 not in rovaniemi:
        if rovaniemi[-1] < fulda[-1]:
            fulda.append(rovaniemi.pop())
            zuege.append(2)
            return

    elif rovaniemi and not fulda and s1 not in rovaniemi:
        fulda.append(rovaniemi.pop())
        zuege.append(2)
        return

    # 3 F -> R
    if fulda and rovaniemi and s1 not in fulda:
        if fulda[-1] < rovaniemi[-1]:
            rovaniemi.append(fulda.pop())
            zuege.append(3)
            return

    elif fulda and not rovaniemi and s1 not in fulda:
        rovaniemi.append(fulda.pop())
        zuege.append(3)
        return

    # 4 R -> N
    if rovaniemi and nordpol and s1 not in rovaniemi:
        if rovaniemi[-1] < nordpol[-1]:
            nordpol.append(rovaniemi.pop())
            zuege.append(4)
            return

    elif rovaniemi and not nordpol and s1 not in rovaniemi:
        nordpol.append(rovaniemi.pop())
        zuege.append(4)
        return

    # Kein Zug ist möglich ohne s1 zu verschieben, daher s1 verschieben
    else:
        bewege_s1()


def bewegen(hat_s1_gezogen):
    """

    :param hat_s1_gezogen: hat s1 im letzten Zug gezogen, dann darf NICHT s1 ziehen -> NICHT s1 zieht nicht zweimal hintereinander
    :return: Gibt zurück ob s1 gezogen hat -> man weiß im nächsten zug ob s1 ziehen muss
    """
    global nordpol
    global rovaniemi
    global fulda
    global s1
    global zuege

    ##########################
    # START  NICHT s1 bewegen
    ##########################
    if hat_s1_gezogen:
        # 1 N -> R
        if nordpol and rovaniemi and s1 not in nordpol:
            if nordpol[-1] < rovaniemi[-1]:
                rovaniemi.append(nordpol.pop())
                zuege.append(1)
                return False

        elif nordpol and not rovaniemi and s1 not in nordpol:
            rovaniemi.append(nordpol.pop())
            zuege.append(1)
            return False

        # NICHT s1
        # 2 R -> F
        if rovaniemi and fulda and s1 not in rovaniemi:
            if rovaniemi[-1] < fulda[-1]:
                fulda.append(rovaniemi.pop())
                zuege.append(2)
                return False

        elif rovaniemi and not fulda and s1 not in rovaniemi:
            fulda.append(rovaniemi.pop())
            zuege.append(2)
            return False

        # NICHT s1
        # 3 F -> R
        if fulda and rovaniemi and s1 not in fulda and s1 not in nordpol:
            if fulda[-1] < rovaniemi[-1]:
                rovaniemi.append(fulda.pop())
                zuege.append(3)
                return False

        elif fulda and not rovaniemi and s1 not in fulda and s1 not in nordpol:
            rovaniemi.append(fulda.pop())
            zuege.append(3)
            return False

        # NICHT s1
        # 4 R -> N
        if rovaniemi and nordpol and s1 not in rovaniemi and s1 not in nordpol:
            if rovaniemi[-1] < nordpol[-1]:
                nordpol.append(rovaniemi.pop())
                zuege.append(4)
                return False

        elif rovaniemi and not nordpol and s1 not in rovaniemi and s1 not in nordpol:
            nordpol.append(rovaniemi.pop())
            zuege.append(4)
            return False

    #######################
    # START s1 bewegen
    #######################

    # s1 bewegen
    # 1 N -> R
    if nordpol and rovaniemi and s1 in nordpol:
        if nordpol[-1] < rovaniemi[-1]:
            rovaniemi.append(nordpol.pop())
            zuege.append(1)
            return True

    elif nordpol and not rovaniemi and s1 in nordpol:
        rovaniemi.append(nordpol.pop())
        zuege.append(1)
        return True

    # s1 bewegen
    # 2 R -> F
    if rovaniemi and fulda and s1 in rovaniemi:
        if rovaniemi[-1] < fulda[-1]:
            fulda.append(rovaniemi.pop())
            zuege.append(2)
            return True

    elif rovaniemi and not fulda and s1 in rovaniemi:
        fulda.append(rovaniemi.pop())
        zuege.append(2)
        return True

    # s1 bewegen
    # 3 F -> R und 4 R -> N werden beide ausgeführt um ziehen im Uhrzeigersinn zu simulieren
    if fulda and rovaniemi and s1 in fulda:
        if fulda[-1] < rovaniemi[-1]:
            # 3 F -> R
            rovaniemi.append(fulda.pop())
            zuege.append(3)
            # 4 R -> N
            nordpol.append(rovaniemi.pop())
            zuege.append(4)
            return True

    elif fulda and not rovaniemi and s1 in fulda:
        # 3 F -> R
        rovaniemi.append(fulda.pop())
        zuege.append(3)
        # 4 R -> N
        nordpol.append(rovaniemi.pop())
        zuege.append(4)
        return True


hat_s1_gezogen = False
while len(nordpol) != 0 or len(rovaniemi) != 0:
    hat_s1_gezogen = bewegen(hat_s1_gezogen)

    print(zuege)
    #print("Zugnr: {} war - {}".format(len(zuege), zuege[-1]))
    #print("Nordpol: {}".format(nordpol))
    #print("Rovaniemi: {}".format(rovaniemi))
    #print("Fulda: {}".format(fulda))


print(zuege)
#
# Mögliche Züge
#


"""
# 1 N -> R
if nordpol and rovaniemi:
    if nordpol[-1] < rovaniemi[-1]:
        rovaniemi.append(nordpol.pop())
        zuege.append(1)
        continue

elif nordpol and not rovaniemi:
    rovaniemi.append(nordpol.pop())
    zuege.append(1)
    continue

# 2 R -> F
if rovaniemi and fulda:
    if rovaniemi[-1] < fulda[-1]:
        fulda.append(rovaniemi.pop())
        zuege.append(2)
        continue

elif rovaniemi and not fulda:
    fulda.append(rovaniemi.pop())
    zuege.append(2)
    continue

# 3 F -> R
if fulda and rovaniemi:
    if fulda[-1] < rovaniemi[-1]:
        rovaniemi.append(fulda.pop())
        zuege.append(3)
        continue

elif fulda and not rovaniemi:
    rovaniemi.append(fulda.pop())
    zuege.append(3)
    continue

# 4 R -> N
if rovaniemi and nordpol:
    if rovaniemi[-1] < nordpol[-1]:
        nordpol.append(rovaniemi.pop())
        zuege.append(4)
        continue

elif rovaniemi and not nordpol:
    nordpol.append(rovaniemi.pop())
    zuege.append(4)
    continue

"""