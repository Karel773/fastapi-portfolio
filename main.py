from fastapi import FastAPI 

app = FastAPI(title = "FastAPI Portoflio Project") 

@app.get("/")
def root():
    return {"status": "ok"}