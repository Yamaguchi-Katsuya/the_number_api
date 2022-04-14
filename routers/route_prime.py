from fastapi import APIRouter
import json
from utils import is_prime


router = APIRouter()


@router.get("/prime/{number}/check")
def check_prime(number: int) -> dict:
    return {"result": is_prime(number)}


@router.get("/prime/{number}/max")
def max_prime(number: int) -> dict:
    if number < 2: return {"result": False}
    current_number = number

    while 2 <= current_number:
        if is_prime(current_number):
            return {"result": current_number}
        current_number -= 1


@router.get("/prime/{number}/list")
def prime_list(number: int) -> dict:
    if number < 2: return {"result": ''}
    prime_number_list = []
    current_number = 2

    while number >= current_number:
        if is_prime(current_number):
            prime_number_list.append(current_number)
        current_number += 1

    return {"result": json.dumps(prime_number_list), "count": len(prime_number_list)}


@router.get("/prime-factorization/{number}")
def prime_factorization(number: int) -> dict:
    prime_factorization = []
    limit = int(number ** 0.5)
    for i in range(2, limit + 1):
        while number % i == 0:
            number /= i
            prime_factorization.append(i)

    if  number >= 2:
        prime_factorization.append(int(number))

    result = ' × ' . join(map(str, prime_factorization))
    return {"result": result}
