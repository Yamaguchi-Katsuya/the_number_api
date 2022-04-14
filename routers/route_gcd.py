from fastapi import APIRouter


router = APIRouter()


@router.get("/gcd/{number1}/{number2}")
def gcd(number1: int, number2: int) -> dict:
	if  number2 == 0: return {"result": number1}
	return gcd(number2, number1 % number2)
