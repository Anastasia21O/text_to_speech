import uvicorn
from fastapi import FastAPI

from api import router

app = FastAPI()

app.include_router(router)

port = 8080

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=port,
        log_level="debug",
        reload=True,
        workers=1,
    )
