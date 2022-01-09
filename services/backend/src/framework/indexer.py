from abc import ABC, abstractmethod
from typing import List, Set, Tuple
from nltk import word_tokenize, pos_tag
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer


class Indexer(ABC):
    def __call__(self, docs_text: List[str]):
        """Take all the bodies of the documents and select the keywords and calculate their weight

        Args:
            docs_text (List[str]): Document body text

        Returns:
            Tuple: A tuple with the weights, idf, tf, and keywords
        """       
        vocabulary = self.extract_vocabulary(docs_text)

        vectorize = TfidfVectorizer(vocabulary=vocabulary)
        weight = vectorize.fit_transform(docs_text)
        idf = vectorize.idf_
        tf = [w / idf for w in weight]
        return (weight, idf, tf, vectorize.get_feature_names_out())

    @abstractmethod
    def extract_vocabulary(self, docs_text: List[str]) -> List[str]:
        pass
    
class NaiveIndexer(Indexer):
    def extract_vocabulary(self, docs_text: List[str]) -> List[str]:
        stop_words = set(stopwords.words('english'))
        words: Set[str] = set()
        for doc in docs_text:
            tokenized = word_tokenize(doc)
            tokenized = [WordNetLemmatizer().lemmatize(w) for w in tokenized]
            tokenized = [token for token in tokenized if not token in stop_words]
            for token in tokenized:
                words.add(token)
        return list(words)     
class NounIndexer(Indexer):

    def extract_vocabulary(self, docs_text: List[str]) -> List[str]:
        """
        Extract the keywords, which in this case are nouns
        """        
        is_noun = lambda pos: pos[:2] == 'NN'
        stop_words = set(stopwords.words('english'))
        nouns: Set[str] = set()
        for doc in docs_text:
            tokenized = word_tokenize(doc)
            tokenized = [WordNetLemmatizer().lemmatize(w) for w in tokenized]
            tokenized = [token for token in tokenized if not token in stop_words]
            for (word, pos) in pos_tag(tokenized):
                if is_noun(pos):
                    nouns.add(word)
        return list(nouns)

