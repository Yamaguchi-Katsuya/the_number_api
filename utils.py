import math


def is_prime(number: int) -> bool:
    if number == 2: return True
    if number < 2 or number % 2 == 0: return False

    for i in range(2, math.ceil(number ** 0.5) + 1):
        if number % i == 0: return False

    return True


def is_perfect(number: int) -> bool:
    if number <= 5: return False
    total: int = 1
    for i in range(2, number):
        if number % i == 0:
            total += i

    return True if total == number else False
