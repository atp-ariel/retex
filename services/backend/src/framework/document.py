from dataclasses import dataclass


@dataclass
class BaseDocument:
    """
    Base class that represents a document, each document has an id, a text, and an author, as well as a type of document that corresponds to the library or test collection to which it belongs.
    """    

    id: int
    title: str
    text: str

    __type__ = "base"

    @classmethod
    def factory(cls, name: str) -> type:
        """Factory of documents, where given a name, it checks all the documents, the one with that type and returns it ready to initialize

        Args:
            name (str): Name of a document type

        Returns:
            [type]: type of document
        """        
        str_class = {}
        for _clss in cls.__subclasses__():
            str_class[_clss.__type__] = _clss

        if not name in str_class:
            raise Exception("Unknown document name")
        
        return str_class[name]

class CranDocument(BaseDocument):
    __type__ = "cran"

    def __init__(self, id: int, title: str, text: str, author: str, editorial: str):
        BaseDocument.__init__(self, id, title.lower(), text.lower())
        self.author = author.lower()
        self.editorial = editorial.lower()

class MedlineDocumnet(BaseDocument):
    __type__ = "med"

    def __init__(self, id: int, text: str):
        BaseDocument.__init__(self, id, text[:50].lower(), text.lower())