from dataclasses import dataclass
from typing import Dict, Iterable, List, Tuple
from . import Query

@dataclass
class CacheValueItem:
    docs: List
    freq: int

class QueryCache:
    def __init__(self, capacity: int = 1024):
        self.__memory__: Dict[Query, CacheValueItem] = {}

        if capacity <= 0:
            raise Exception("Capacity must be positive")

        self.capacity = capacity 
        
    def __check_full_memory__(self) -> bool:
        return len(self.__memory__) >= self.capacity

    def add_query(self, qry: Query, result: List):
        if self.__check_full_memory__():
            self.__delete_query__()
        
        self.__memory__[qry] = CacheValueItem(result, 1)

    def __delete_query__(self):
        min = (None, float("inf"))
        for key in self.__memory__.keys():
            if self.__memory__[key].freq < min[1]:
                min = (key, self.__memory__[key].freq)

        del self.__memory__[min[0]]

        if self.__check_full_memory__():
            self.__delete_query__()

    def __getitem__(self, qry: Query) -> List:
        if qry in self.__memory__:
            self.__memory__[qry].freq += 1
            return self.__memory__[qry].dcos

    def __iter__(self) -> Iterable[Query]:
        for qry in self.__memory__.keys():
            yield qry

    def contains(self, qry: str) -> Tuple[bool, Query]:
        qry = qry.lower()
        for q in self:
            if q.text == qry:
                return (True, q)
        return (False, None)

    def clear(self):
        self.__memory__.clear()