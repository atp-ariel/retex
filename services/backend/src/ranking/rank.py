from typing import List
from heapq import nlargest
from sklearn.metrics.pairwise import cosine_similarity
from ..framework import FrameworkManager, BaseDocument
from ..query import Query

class RankManager:
    def __init__(self, top: int):
        self.top: int = top
    
    def get_posting_list(self, framework: FrameworkManager, qry: Query, wq) -> List[BaseDocument]:
        wc = framework.weigths
        cos = cosine_similarity(wc, wq.reshape(1, -1))

        doc_cos = []
        for i in range(len(framework.collection)):
            doc = framework.collection[i]
            sim = cos[i]
            doc_cos.append((doc, sim))

        top = nlargest(self.top, doc_cos, key=lambda x: x[1])
        top = list(map(lambda t: t[0], top))
        return top