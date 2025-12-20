from twttr import shorten


def test_shorten():
    assert shorten("Hello World") == "Hll Wrld"
    assert shorten("AEIOUaeiou") == ""
    assert shorten("Python") == "Pythn"
    assert shorten("") == ""
    assert shorten("1234aio") == ("1234")
    assert shorten("!sdew") == ("!sdw")
    assert shorten("Twttr") == "Twttr"

