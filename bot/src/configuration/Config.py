import os
from dotenv import load_dotenv

from configuration.СhangeError import СhangeError
from configuration.Postgres import Postgres

load_dotenv()

class Config:
    debug: str = None
    token: str = None
    postgres: Postgres = None

    def __init__(self):
        self._debug = os.getenv("debug")
        self._token = os.getenv("token")
        self._postgres = Postgres()

    @property
    def debug(self):
        return self._debug
    
    @debug.setter
    def debug(self, value):
        raise СhangeError()
    
    @property
    def token(self):
        return self._token
    
    @token.setter
    def token(self, value):
        raise СhangeError()
    
    @property
    def postgres(self):
        return self._postgres
    
    @postgres.setter
    def postgres(self, value):
        raise СhangeError()