import os
import hashlib

import pytest


from PythonTesting.src.check_filenumber import (
    more_lines_than_limit
    )


def test_more_lines_than_limit(): 
    assert more_lines_than_limit('data/test\\testfile0.txt', 5) is False
    assert more_lines_than_limit('data/test\\testfile1.txt', 5) is True
    assert more_lines_than_limit('data/test\\testfile2.txt', 5) is False
    with pytest.raises(ValueError): 
        more_lines_than_limit('data/test\\testfile2.txt', -1)
    with pytest.raises(ValueError): 
        more_lines_than_limit('data/test\\testfile2.txt', "a")