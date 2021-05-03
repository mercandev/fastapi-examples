from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def FirstMethod():
    return {"Message": "Hello World"}
