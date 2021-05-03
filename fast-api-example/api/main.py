from fastapi import FastAPI

app = FastAPI()

@app.get("/")
    return {"Message": "Hello World"}
