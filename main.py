from fastapi import FastAPI 
from enum import Enum

app = FastAPI()

@app.get("/")
def home():
    return "Hello World"


@app.get("/items/{id}")
def items(id: int):
    return f"The ID is: {id}"


class CarName(str, Enum):
    audi = "Audi"
    vw = "Volkswagen"
    bmw = "BMW"

@app.get("/carmodels/{car_name}")
def get_car_name(car_name: CarName):
    if car_name is CarName.audi:
        return f"The brand you chose is: {car_name}"
    elif car_name == "Volkswagen":
        return f"The brand you chose is: {car_name}"
    elif car_name is CarName.bmw:
        return f"The brand you chose is: {car_name}"