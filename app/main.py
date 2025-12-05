from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "hello world"}

@app.get("/sum")
def sum_two_numbers(a: int, b: int):
    return {"result": a + b}
