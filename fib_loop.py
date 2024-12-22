import time


def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1

    prev, curr = 1, 1
    for _ in range(3, n + 1):
        prev, curr = curr, prev + curr
    return curr


if __name__ == "__main__":
    while True:
        try:
            n = int(input("Введите номер числа Фибоначчи (1 ≤ n ≤ 40) или 0 для выхода: "))
            if n == 0:
                print("Выход из программы.")
                break
            elif n < 1 or n > 32:
                print("Пожалуйста, введите число от 1 до 40.")
                continue

            start_time = time.time()
            result = fib(n)
            elapsed_time = (time.time() - start_time) * 1000

            print(f"fib({n}) = {result}, время выполнения: {elapsed_time:.3f} мс")
        except ValueError:
            print("Некорректный ввод. Введите целое число от 1 до 40.")
