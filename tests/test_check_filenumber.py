import os
import hashlib

import pytest


from PythonTesting.src.check_filenumber import (
    more_lines_than_limit, 
    del_spaces
    )


def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def test_more_lines_than_limit(): 
    assert more_lines_than_limit('data/test\\testfile0.txt', 5) is False
    assert more_lines_than_limit('data/test\\testfile1.txt', 5) is True
    assert more_lines_than_limit('data/test\\testfile2.txt', 5) is False
    with pytest.raises(ValueError): 
        more_lines_than_limit('data/test\\testfile2.txt', -1)
    with pytest.raises(ValueError): 
        more_lines_than_limit('data/test\\testfile2.txt', "a")


def test_del_spaces():
    ### create dummy file for testing
    path_to_testing = os.path.join(os.getcwd(), "tests")
    dummy_file = os.path.join(path_to_testing, "dummy_file.txt")
    with open(dummy_file, "w", encoding="utf-16le") as f:
        f.write("Hallo" + "\t" + "Welt" + "\t" + "123\n")
        f.write("test" + "\t" + "" + "\t" + "abcdef")
    expected_hash = md5(dummy_file)

    dummy_file_spaces = os.path.join(path_to_testing, "dummy_file_spaces.txt")
    with open(dummy_file_spaces, "w", encoding="utf-16le") as fs: 
        fs.write("H a l l o" + "\t" + "W e l t" + "\t" + "1 2 3\n")
        fs.write("t e s t" + "\t" + "" + "\t" + "a b c d e f")

    cleaned_file = del_spaces(dummy_file_spaces)
    assert md5(cleaned_file) == expected_hash

    ### remove created dummy files
    os.remove(dummy_file)
    os.remove(dummy_file_spaces)
    os.remove(cleaned_file)