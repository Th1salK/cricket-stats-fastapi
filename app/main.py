from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Cricket stat api is working."}
