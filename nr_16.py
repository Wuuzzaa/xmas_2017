# siehe zur Erklärung nr_16.jpg
# tl;dr die 3 funktionen sind nur abhänig von der dasher funktion
def calc_a(n):
    sequence = [2, 4, 7]
    for i in range(3, n+1):
        sequence.append(2*sequence[i-1] - sequence[i-3])
    return sequence

print(calc_a(88)[-1]) # bis 88, da ich bei 0 anfange zu zählen



