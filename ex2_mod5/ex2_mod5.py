from typing import Callable
import re

def generator_numbers(text: str):
    numbers = [float(number) for number in re.findall((r"\d+\.\d+\s"), text)]    #  ідентифікували дійсні числа у тексті і перевели у float
    for number in numbers:
        yield number                                                              # створили генератор чисел
    
    
def sum_profit(text: str, func: Callable):
    return sum(func(text))                                                        # рахуємо суму чисел


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
