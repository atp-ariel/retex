from services.backend.src.framework import FrameworkManager

from pathlib import Path

CRAN_PATH = Path("db/cran/cran.all.1400")
CRAN_TYPE = "cran"

DOC_ID = 563
DOC_TITLE = "the law of the wake in the turbulent boundary layer ."
DOC_AUTHOR = "coles,d."
DOC_EDITORIAL = "j. fluid mech. 1, 1956,191."

def test_framework_across():
    f = FrameworkManager(CRAN_PATH, CRAN_TYPE)

    assert len(f.collection) == 1400 and f.weigths.shape[0] == 1400

    doc_563 = f.collection[DOC_ID - 1]
    
    assert doc_563.id == DOC_ID and doc_563.title == DOC_TITLE