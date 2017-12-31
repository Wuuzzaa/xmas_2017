def fibonacci_1_grad(n):
    sequence = [0, 1, 1]
    for i in range(3, n+1):
        sequence.append(sequence[i-1] + sequence[i-2])
    return sequence


def fibonacci_2_grad(n, fib_zahlen_1_grad):
    sequence = [0, 1]
    for i in range(2, n+1):
        sequence.append(sequence[i-1] + sequence[i-2] + fib_zahlen_1_grad[i])
    return sequence

# Fibonaccizahlen zweiter Ordnung bis 80 berechnen
fib_zahlen_2_grad = fibonacci_2_grad(80, fibonacci_1_grad(80))

print("80. Fibonaccizahl zweiter Ordnung ist: {}".format(fib_zahlen_2_grad[-1]))

