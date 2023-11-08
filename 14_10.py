def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def golden_ratio(i):
    fibonacci_i = fibonacci(i)
    fibonacci_i_plus_1 = fibonacci(i+1)

    golden_ratio = fibonacci_i_plus_1 / fibonacci_i

    print("The golden ratio approximation for", i, "is:", golden_ratio)

# Пример использования функции
golden_ratio(3)