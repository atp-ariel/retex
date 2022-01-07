from abc import ABC, abstractmethod
from typing import List, Set, Tuple
from nltk import word_tokenize, pos_tag
from sklearn.feature_extraction.text import TfidfVectorizer


class Indexer(ABC):
    @abstractmethod
    def __call__(self, docs_text: List[str]):
        pass

class NounIndexer(Indexer):
    def __call__(self, docs_text: List[str]) -> Tuple:
        """Take all the bodies of the documents and select the keywords and calculate their weight

        Args:
            docs_text (List[str]): Document body text

        Returns:
            Tuple: A tuple with the weights and keywords
        """        
        nouns = self.__extract_nouns__(docs_text)

        vectorize = TfidfVectorizer(vocabulary=nouns)
        weight = vectorize.fit_transform(docs_text)
        return (weight, vectorize.get_feature_names_out())


    def __extract_nouns__(self, docs_text: List[str]) -> List[str]:
        """
        Extract the keywords, which in this case are nouns
        """        
        is_noun = lambda pos: pos[:2] == 'NN'
        
        nouns: Set[str] = set()
        for doc in docs_text:
            tokenized = word_tokenize(doc)
            for (word, pos) in pos_tag(tokenized):
                if is_noun(pos):
                    nouns.add(word)
        return list(nouns)

