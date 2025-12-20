from plates import is_valid


def test_alpha():
    assert is_valid("AA") == True
    assert is_valid("A1") == False
    assert is_valid("12") == False

def test_length():
    assert is_valid("CS50") == True
    assert is_valid("C") == False
    assert is_valid("PYTHON") == True
    assert is_valid("OUTATIME") == False

def test_numbers():
    assert is_valid("AAA222") == True
    assert is_valid("AAA022") == False
    assert is_valid("AAA22A") == False

def test_punctuation():
    assert is_valid("CS50!") == False
    assert is_valid("CS 50") == False
    assert is_valid("PI3.14") == False
