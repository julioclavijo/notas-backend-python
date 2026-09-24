from fastapi import FastAPI
from routes.routes import router

app = FastAPI(title="API de tareas")
app.include_router(router)

@app.get("/")
def root():
    return {"mensaje": "bienvenido a la API de tareas"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
        log_level="info"
    )