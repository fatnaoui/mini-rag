from fastapi import FastAPI
app = FastAPI()

@app.get("/welcome")
def hello():
    return {
        "key":"Hello All"
    }