# створюємо функцію кешування
def caching_fibonacci():
    # створюємо словник для кешу
    cache = {}
    
    # створюємо функцію для обчислення чисел Фібоначчі
    def fibonacci(n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        # перевіряємо чи є число в кеші
        if n in cache:
            return cache[n]
        
        # зберігаємо результат обчислення чисел Фібоначчі в кеш
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        # повертаємо значення з кешу
        return cache[n]
        
    # повертаємо внутрішню функцію fibonacci з урахуванням використання кешу
    return fibonacci

# Отримуємо функцію fibonacci
fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))
print(fib(15))
