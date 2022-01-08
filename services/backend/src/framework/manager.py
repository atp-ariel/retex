from pathlib import Path
from typing import List, Tuple
from . import BaseDocument
from .collection import DocCollection
from .parsers import BaseParser
from .indexer import NounIndexer

class FrameworkManager:
    def __init__(self, doc_path: Path, type: str):
        self.__type__ = type
        self.path = doc_path

        # Get document from db
        docs = self.__get_documents__()

        # Initializate DocCollection
        self.collection = DocCollection(docs)

        # Get stats for collection        
        indexer = NounIndexer()
        self.weigths, self.idf, self.tf, self.K = indexer(self.collection.bodies)

    def get_stats(self, index: int) -> Tuple[DocCollection, List[float]]:
        """Obtain the weights of a document given a collection index

        Args:
            index (int): Index in the collection of the desired document

        Returns:
            Tuple[DocCollection, List[float]]: A tuple with the result of indexing in FrameworkManager, the tuple has two elements, the document in question and the corresponding array of weights
        """        
        return (self.collection[index], self.weigths[index])

    def __get_documents__(self) -> List[BaseDocument]:
        """Get the documents that are in the file path. Said file is parsed depending on which collection it is and each document is converted to its corresponding class in the model.

        Returns:
            List[BaseDocument]: List of documents in file path
        """        
        if not self.path.exists() or not self.path.is_file():
            raise Exception("Document collections path is nonexistent")
        
        # Open path and read content
        fcontent = str()
        with open(self.path, "r", encoding='utf8') as fpath:
            fcontent = fpath.read()

        return BaseParser.factory(self.__type__)(fcontent)



        
        
