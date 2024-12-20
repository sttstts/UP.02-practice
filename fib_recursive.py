import time

def fib(n):
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def measure_time_for_fib(n):

    start_time = time.time()
    result = fib(n)
    end_time = time.time()
    elapsed_time = (end_time - start_time) * 1000
    print(f"fib({n}) = {result}, время выполнения: {elapsed_time:.2f} ms")

if __name__ == "__main__":
    while True:
        try:
            user_input = input("Введите целое число от 1 до 24 (или 'exit' для выхода): ")
            if user_input.lower() == 'exit':
                print("Выход из программы.")
                break
            n = int(user_input)
            if 1 <= n <= 40:
                measure_time_for_fib(n)
            else:
                print("Ошибка: число должно быть от 1 до 40.")
        except ValueError:
            print("Ошибка: введите целое число.")
