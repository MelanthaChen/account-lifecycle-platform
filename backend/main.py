from fastapi import FastAPI

app = FastAPI(
    title="Account Lifecycle Platform",
    version="1.0.0"
)

@app.get("/")
def health_check():
    return {
        "status": "running"
    }