from dataclasses import dataclass
import re
from statistics import mean
from typing import Dict, List, Set
from numpy import array, zeros
from .metrics import Precission, Recall, F1Mean, FMean
from .config import Config
from .retex import Retex


@dataclass
class Qry:
    id: int
    text: str

    def __eq__(self, other):
        if isinstance(other, Qry):
            return self.id == other.id
        raise TypeError
    
    def __hash__(self) -> int:
        return self.id

class Evaluator:
    def __init__(self, type: str):
        self.__type__ = type
        self.queries : List[Qry] = self.get_queries()
        self.rel : Dict[int, List[int]] = self.get_rel()

    def get_queries(self) -> List[Qry]:
        fcontent = str()
        with open(Config().get_qry_path(self.__type__)) as f:
            fcontent = f.read()

        I = re.compile("\.I")
        W = re.compile("\\n\.W\\n")


        qry = []
        fsplit = re.split(I, fcontent)[1:]

        for item in fsplit:
            temp = re.split(W, item)
            qry.append(Qry(int(temp[0]), temp[1]))

        return qry
    
    def get_rel(self) -> Dict[int, List[int]]:
        fcontent = []
        with open(Config().get_rel_path(self.__type__)) as f:
            fcontent = f.readlines()

        result = {}
        for line in fcontent:
            line_splitted = line.split()
            qry, doc = int(line_splitted[0]), int(line_splitted[1])
            if qry in result.keys():
                result[qry].append(doc)
            else:
                result[qry] = [doc]
        return result

    def evaluate(self, retex: Retex) -> Dict[str, float]:
        metrics = array([Precission(), Recall(), FMean(), F1Mean()])

        results = [[],[],[],[]]
        for i in self.rel.keys():
            if Qry(i, "") in self.queries:
                qry = self.queries[self.queries.index(Qry(i, ""))]
                docs = list(map(lambda doc: doc.id, retex.do_query(qry.text)))
                for i, m in enumerate(metrics):
                    print(m)
                    results[i].append(m(docs, self.rel[qry.id]))

        evaluation = {
            "P": mean(results[0]),
            "R": mean(results[1]),
            "F": mean(results[2]),
            "F1": mean(results[3])
        }
        return evaluation