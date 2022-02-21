from typing import List, Tuple

from numpy import multiply
from . import Query
from ..framework import FrameworkManager
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from nltk import word_tokenize, pos_tag
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer

class QueryManager:
    def __init__(self, alpha: float, frame: FrameworkManager):
        if not 0.0 <= alpha <= 1.:
            raise Exception("Alpha must be in [0, 1]")
        self.alpha = alpha
        self.frame = frame
        self.vocabulary = self.frame.K

    def __call__(self, text: str) -> Tuple[Query, List[float]]:

        qry = Query(text.lower())
        qry = self.preprocess_query_text(qry)

        weight = self.get_weight(qry)

        return (qry, weight)
    
    def get_weight(self, qry: Query):
        vectorize = TfidfVectorizer(vocabulary=self.vocabulary)
        weight = vectorize.fit_transform([qry.text])
        
        tf = weight / self.frame.idf

        w = (1 - self.alpha) * tf
        w += self.alpha
        w = multiply(w, tf)
        return w

    def preprocess_query_text(self, qry: Query) -> Query:
        text = qry.text

        stop_words = set(stopwords.words('english'))
        tokenized = word_tokenize(text)
        tokenized = [WordNetLemmatizer().lemmatize(w) for w in tokenized]
        tokenized = [token for token in tokenized if not token in stop_words]

        qry.text = " ".join(tokenized)
        return qry

