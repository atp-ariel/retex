from typing import Type

class Query:
    def __init__(self, text: str):
        self.text = text.lower()
        
    def __getitem__(self, index: int) -> str:
        return self.text[index]
        
    def __eq__(self, other) -> bool:
        if not isinstance(other, Query):
            raise TypeError("other must be a Query")
        
        return self.text == other.text
    
    def __hash__(self) -> int:
        return self.text.__hash__()
    
    def __str__(self) -> str:
        return self.text
    
    def __repr__(self):
        return self.__str__()