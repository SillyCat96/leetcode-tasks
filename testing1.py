def fibonacci(n):
    if n <= 0:
        return "Некорректный ввод"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Пример использования функции для вычисления 10 чисел Фибоначчи
for i in range(1, 11):
    print(f"Число Фибоначчи {i}: {fibonacci(i)}")
