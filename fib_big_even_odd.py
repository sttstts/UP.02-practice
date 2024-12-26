def fib_eo(n):
    a, b = 0, 1

    for _ in range(n):
        a, b = b, (a + b) % 10

    if a % 2 == 0:
        print("even")
    else:
        print("odd")

if __name__ == "__main__":
    try:
        n = int(input("Введите число n (1 ≤ n ≤ 10^6): "))
        if 1 <= n <= 10 ** 6:
            fib_eo(n)
        else:
            print("Ошибка: число должно быть в диапазоне от 1 до 10^6.")
    except ValueError:
        print("Ошибка: введите корректное целое число.")
