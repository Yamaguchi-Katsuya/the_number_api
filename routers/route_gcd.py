from fastapi import APIRouter
from pydantic import BaseModel


class Gcd(BaseModel):
    number1: int
    number2: int


router = APIRouter()


@router.post('/gcd')
def index(gcd: Gcd) -> dict:
	return getGcd(gcd.number1, gcd.number2)


def getGcd(number1: int, number2: int) -> dict:
	if  number2 == 0: return {"result": number1}
	return getGcd(number2, number1 % number2)
