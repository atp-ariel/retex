from typing import List
from . import BaseDocument


class DocCollection:
    # region Overloads
    def __len__(self) -> int:
        """
        Returns the number of documents in the collection
        """
        return len(self.__docs__)

    def __getitem__(self, i: int) -> BaseDocument:
        """Index in the document collection

        Args:
            i (int): Desired index

        Returns:
            BaseDocument: Document that is in position i of the collection
        """
        return self.__docs__[i]

    def __iter__(self) -> List[BaseDocument]:
        """
        The class is an iterable of documents
        """        
        return self.__docs__
    # endregion Overloads

    @property
    def bodies(self) -> List[str]:
        """
        Returns a list with all the text bodies of the documents
        """        
        return list(map(lambda doc: doc.text, self.__docs__))

    def __init__(self, docs: List[BaseDocument]):
        self.__docs__: List[BaseDocument] = docs
