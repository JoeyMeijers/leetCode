from valid_anagram import valid_anagram


def test_valid_anagram():
    s: str = "racecar"
    t: str = "carrace"
    assert valid_anagram(s, t) is True

    s: str = "jar"
    t: str = "jam"
    assert valid_anagram(s, t) is False
    print("yaay")
