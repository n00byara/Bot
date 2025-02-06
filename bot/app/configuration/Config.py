import os
from dotenv import load_dotenv

from configuration import СhangeError

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

dotenv_path = os.path.join(f"{BASE_DIR}/config", ".env")
load_dotenv(dotenv_path)

class Config:
    token: str = None

    def __init__(self) -> None:
        self._token = os.getenv("TOKEN")

    @property
    def token(self) -> str:
        return self._token
    
    @token.setter
    def token(self, value) -> None:
        raise СhangeError()