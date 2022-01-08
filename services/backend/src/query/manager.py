from typing import List, Tuple
from . import Query
from ..framework import FrameworkManager
from sklearn.feature_extraction.text import CountVectorizer
from numpy import array, argmax


class QueryManager:
    def __init__(self, alpha: float, frame: FrameworkManager):
        if not 0.0 <= alpha <= 1.:
            raise Exception("Alpha must be in [0, 1]")
        self.alpha = alpha
        self.frame = frame
        self.vocabulary = self.frame.K

    def __call__(self, text: str) -> Tuple[Query, List[float]]:

        qry = Query(text)

        vectorize = CountVectorizer(vocabulary=self.vocabulary)

        global_freq = vectorize.fit_transform(self.frame.collection.bodies)
        freq = vectorize.fit_transform(qry.text)

        index_horizontal = argmax(global_freq)
        row = index_horizontal // global_freq.shape[0]
        col = index_horizontal % global_freq.shape[1]

        max_f = global_freq[row, col]
        f_max = freq[col]
        tf = array([self.alpha + (1 - self.alpha)*(f/max_f*f_max)
                    for f in freq])

        weight = tf * self.frame.idf

        return (qry, weight)
