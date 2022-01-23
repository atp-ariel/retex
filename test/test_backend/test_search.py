import pytest
from services.backend.src.main import search

def test_q_1():
    q = "what similarity laws must be obeyed when constructing aeroelastic models of heated high speed aircraft ."
    docs = [184, 29, 31, 12, 51, 102, 13, 14, 15, 57, 378, 859, 185, 30, 37, 52, 142,195, 875, 56, 66, 95, 462, 497, 858, 876, 879,880, 486]
    
    result = search(q)

    assert len(result) == 1400

    i = 0
    for doc in result:
        if doc in docs:
            i += 1
    assert i > 0