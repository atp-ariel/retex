import re
from typing import Dict, List
from abc import ABC, abstractmethod
from . import BaseDocument


class BaseParser(ABC):
    __type__ = "base"

    @abstractmethod
    def __call__(self, text: str) -> List[BaseDocument]:
        pass

    @classmethod
    def factory(cls, name: str):
        str_class = {}
        for _clss in cls.__subclasses__():
            str_class[_clss.__type__] = _clss

        if not name in str_class:
            raise Exception("Unknown parser name")
        
        return str_class[name]()

class CranParser(BaseParser):
    __type__ = "cran"
    
    def __init__(self):
        self.__type_doc__ = BaseDocument.factory(CranParser.__type__)
        self.RE_T = re.compile("\.T")
        self.RE_A = re.compile("\.A")
        self.RE_B = re.compile("\.B")
        self.RE_W = re.compile("\.W")

    def __call__(self, text: str) -> List[BaseDocument]:
        """Return a list of base document
        """
        dict_docs = self.tokenize_docs(text)

        docs = []
        for i, dd in enumerate(dict_docs):
            docs.append(self.__type_doc__(i + 1, dd["T"], dd["W"], dd["A"], dd["T"]))
        return docs


    def tokenize_docs(self, text: str) -> List[Dict[str, str]]:
        """Document tokenizer, returns a dictionary of tokens for each document

        """
        docs_splitted = re.split("\.I [0-9]*", text)[1:]

        for doc in docs_splitted:
            doc = re.split(self.RE_T, doc)[1]
            T, doc = re.split(self.RE_A, doc, 1)
            A, doc = re.split(self.RE_B, doc, 1)
            B, W = re.split(self.RE_W, doc, 1)

            T = T.replace("\n", "")
            A = A.replace("\n", "")
            B = B.replace("\n", "")
            W = W.replace("\n", "")

            yield {"T": T, "A": A, "B": B, "W": W}