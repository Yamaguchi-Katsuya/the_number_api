from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from decouple import config
from routers import route_gcd, route_prime, route_perfect


app = FastAPI()
app.include_router(route_gcd.router)
app.include_router(route_prime.router)
app.include_router(route_perfect.router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=config('ALLOW_ORIGINS').split(','),
    allow_methods=['POST', 'GET'],
)
