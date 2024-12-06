from typing import List
from group_anagrams import group_anagrams
from two_sum import twoSum
from contains_duplicate import contains_duplicate
from encode_and_decode_strings import encode, decode
from top_k_frequent_elements import top_k_frequent_elements
from valid_anagram import valid_anagram


def test_two_sum():
    nums: List[int] = [1, 3, 6, 8]
    target: int = 11
    expected_result: List[int] = [1, 3]

    result: List[int] = twoSum(nums, target)

    assert expected_result == result


def test_contains_duplicate():
    input_true: List[int] = [1, 2, 3, 1]
    input_false: List[int] = [1, 2, 3, 4]

    assert (contains_duplicate(input_true))
    assert (contains_duplicate(input_false) == False)


def test_encode_decode_strings():
    input = ["we", "say", ":", "yes"]
    output = ["we", "say", ":", "yes"]

    result = encode(input)
    result = decode(result)
    assert input == result

    input = ["we", "say", ":", "yes", "!@#$%^&*()"]
    output = ["we", "say", ":", "yes", "!@#$%^&*()"]
    result = encode(input)
    result = decode(result)
    assert input == result

def test_group_anagrams():
    input: List[str] = ["act", "pots", "tops", "cat", "stop", "hat"]
    expected_output: List[List[str]] = [
        ["hat"], ["act", "cat"], ["pots", "tops", "stop"]
    ]

    output: List[List[str]] = group_anagrams(input)

    assert sorted(output) == sorted(expected_output)

def test_top_k_frequent_elements():
    nums = [1, 2, 2, 3, 3, 3]
    k = 2
    result = top_k_frequent_elements(nums, k)
    expected = [2, 3]
    assert sorted(result) == sorted(result)

def test_valid_anagram():
    s: str = "racecar"
    t: str = "carrace"
    assert valid_anagram(s, t) is True

    s: str = "jar"
    t: str = "jam"
    assert valid_anagram(s, t) is False
    print("yaay")