from fastapi import FastAPI

app = FastAPI()

@app.post("/hello")
def say_hello(name: str):
    return {"msg": f"Hello {name}"}
