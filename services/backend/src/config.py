from .utils import Singleton
from json import load
from pathlib import Path

@Singleton
class Config:
    def __init__(self):
        self.__dict__ = load(open("./src/config.json", "r"))

    def get_db_path(self, name: str) -> Path:
        return Path(self.db[name]["path"])
    def get_qry_path(self, name: str) -> Path:
        return Path(self.db[name]["qry"])

    def get_rel_path(self, name: str) -> Path:
        return Path(self.db[name]["rel"])

    def get_alpha(self) -> float:
        return self.alpha

    def get_top(self) -> int:
        return self.top

    def get_umbral(self) -> float:
        return self.umbral