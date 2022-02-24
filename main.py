from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import math
import json
import sys


app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/prime/{number}/check")
def check_prime(number: int):
    return {"result": is_prime(number)}

@app.get("/prime/{number}/max")
def max_prime(number: int):
    if number < 2: return {"result": False}
    current_number = number

    while 2 <= current_number:
        if is_prime(current_number):
            return {"result": current_number}
        current_number -= 1

@app.get("/prime/{number}/list")
def prime_list(number: int):
    if number < 2: return {"result": ''}
    prime_number_list = []
    current_number = 2

    while number >= current_number:
        if is_prime(current_number):
            prime_number_list.append(current_number)
        current_number += 1

    return {"result": json.dumps(prime_number_list)}

def is_prime(number: int) -> bool:
    if number == 2: return True
    if number < 2 or number % 2 == 0: return False

    for i in range(2, math.ceil(number ** 0.5) + 1):
        if number % i == 0: return False

    return True
