import re
from typing import Callable

def generator_numbers(text: str):
    # знаходження всіх дійсних чисел в тексті, запис їх як рядок у список
    for numbers in re.findall(r'\d+\.\d+', text):
        # створення генератора та перетворення рядка на числа з крапкою
        yield float(numbers)

def sum_profit(text: str, func: Callable):
    # обчислення загальної суми чисел
    total_sum = sum(func(text))
    return total_sum

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
