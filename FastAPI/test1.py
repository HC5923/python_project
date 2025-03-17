from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"index": "FastAPI 안녕"}


@app.get("/math/sum")
def math_sum(number_1: int, number_2: int):
    return {"result": number_1 + number_2}
    