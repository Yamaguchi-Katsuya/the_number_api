from fastapi import APIRouter
import json
from utils import is_perfect


router = APIRouter()


@router.get('/perfect/{number}/check')
def perfect_check(number: int):
    return {"result": is_perfect(number)}


@router.get('/perfect/{number}/max')
def max_perfect(number: int):
    if number <= 5: return {"result": False}
    current_number = number

    while 5 <= current_number:
        if is_perfect(current_number):
            return {"result": current_number}
        current_number -= 1


@router.get("/perfect/{number}/list")
def perfect_list(number: int) -> dict:
    if number <= 5: return {"result": ''}
    perfect_number_list = []
    current_number = 6

    while number >= current_number:
        if is_perfect(current_number):
            perfect_number_list.append(current_number)
        current_number += 1

    return {"result": json.dumps(perfect_number_list), "count": len(perfect_number_list)}
