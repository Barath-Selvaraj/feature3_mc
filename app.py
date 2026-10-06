from fastapi import FastAPI

app = FastAPI(
    title="Feature 3 Service"
)


@app.get("/")
def root():
    return {
        "feature": "feature3",
        "message": "Feature 3 is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }