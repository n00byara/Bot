from fastapi import FastAPI
import uvicorn

from configuration.Config import Config
from db.DB import DB

config = Config()
db = DB()
app = FastAPI()

@app.get("/")
async def root():
    return db.get_users()

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=config.host,
        port=config.port,
        log_level=config.log_level,
        reload=config.debug
    )