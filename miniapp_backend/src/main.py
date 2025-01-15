from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from uvicorn import run

from configuration.Config import Config
from db.DB import DB

config = Config()
db = DB()
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return db.get_users()

if __name__ == "__main__":
    run(
        "main:app",
        host=config.host,
        port=config.port,
        log_level=config.log_level,
        reload=config.debug
    )