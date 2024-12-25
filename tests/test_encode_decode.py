from encode_and_decode_strings import encode, decode
from typing import List


def test_encode_decode_strings():
    input = ["we", "say", ":", "yes"]

    result = encode(input)
    result = decode(result)
    assert input == result

    input = ["we", "say", ":", "yes", "!@#$%^&*()"]
    result = encode(input)
    result = decode(result)
    assert input == result
