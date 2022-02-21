from pathlib import Path
from typing import List
from .framework import FrameworkManager, BaseDocument
from .query import QueryCache, QueryManager
from .ranking import RankManager
from .utils import Singleton
from .config import Config

from nltk import download, data



@Singleton
class Retex:
    def __init__(self, __type__: str):
        #region Download resource before use
        try:
            data.find('tokenizers/punkt')
        except LookupError:
            download('punkt')

        try:
            data.find("corpora/omw-1.4")
        except LookupError:
            download('omw-1.4')

        try:
            data.find("corpora/wordnet")
        except LookupError:
            download("wordnet")

        try:
            data.find("taggers/averaged_perceptron_tagger")
        except LookupError:
            download('averaged_perceptron_tagger')

        try:
            data.find("corpora/stopwords")
        except LookupError:
            download("stopwords")
        #endregion
        self.__type__ = __type__
        path = Config().get_db_path(self.__type__)
        
        self.framework: FrameworkManager = FrameworkManager(path, self.__type__)
        
        self.qry_manager: QueryManager = QueryManager(Config().get_alpha(), self.framework)
        
        self.cache: QueryCache = QueryCache(3)
        self.ranker: RankManager = RankManager(Config().get_top())

    def do_query(self, text_query: str) -> List[BaseDocument]:
        contains, query = self.cache.contains(text_query)
        if contains:
            return self.cache[query]
        
        query, wq = self.qry_manager(text_query)
        docs = self.ranker.get_posting_list(self.framework, query, wq)
        
        # Add to cache
        self.cache.add_query(query, docs)
        return docs