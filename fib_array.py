def fib(n):
    if n < 1 or n > 40:
        raise ValueError("n должно быть в пределах от 1 до 40")

    fib_sequence = [0] * (n + 1)

    fib_sequence[0] = 0
    if n > 0:
        fib_sequence[1] = 1

    for i in range(2, n + 1):
        fib_sequence[i] = fib_sequence[i - 1] + fib_sequence[i - 2]

    print(fib_sequence)
    return fib_sequence

if __name__ == "__main__":
    try:
        n = int(input("Введите число n (от 1 до 40): "))
        fib(n)
    except ValueError as e:
        print(e)
