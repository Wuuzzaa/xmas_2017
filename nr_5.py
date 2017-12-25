file_path = "data/random.txt"

file = open(file_path)
zeilen = file.readlines()
zahlen = []


def fibonacci(n):
    sequence = [0,1,1]
    for i in range(3, n+1):
        sequence.append(sequence[i-1] + sequence[i-2])
    return sequence

print("Ausgangsproblem: {} Zahlen vorhanden".format(len(zeilen)))

# negative zahlen/zeilen löschen
for zeile in zeilen:
    if int(zeile) > 0:
        zahlen.append(int(zeile))

print("Negative Zahlen entfernt - Noch {} Zahlen vorhanden".format(len(zahlen)))

# sortieren
zahlen.sort()

# Fibonaccizahlen bis maximum berechnen ca. 92 Fibonaccizahl (google)
fib_zahlen = fibonacci(92)

# von hinten prüfen ob zahl primzahl ist
for i in range(len(zahlen)-1, 0, -1):
    if zahlen[i] in fib_zahlen:
        print("Höchste Fibonaccizahl ist: {}".format(zahlen[i]))
        break
