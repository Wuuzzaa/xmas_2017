def fibonacci(n):
    sequence = [0, 1, 1]
    for i in range(3, n+1):
        sequence.append(sequence[i-1] + sequence[i-2])
    return sequence

# Fibonaccizahlen bis maximum berechnen 93 Fibonaccizahl (google) , da max < fib(94)
fib_zahlen = fibonacci(93)
fib_zahlen.reverse()

zahl = 12345678901234567890
rest = zahl
loesung = ""

for i in range(len(fib_zahlen)):
    # rest >= fib
    if rest >= fib_zahlen[i]:
        loesung += "1"
        rest -= fib_zahlen[i]

    # rest < fib
    else:
        loesung += "0"

# die 2 rechten zeichen abschneiden
loesung = loesung[:-2]

print("Fibonaccidarstellung von {} ist \n{}".format(zahl, loesung))
