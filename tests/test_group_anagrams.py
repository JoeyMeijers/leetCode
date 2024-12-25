from group_anagrams import group_anagrams
from typing import List


def test_group_anagrams():
    input: List[str] = ["act", "pots", "tops", "cat", "stop", "hat"]
    expected_output: List[List[str]] = [
        ["hat"], ["act", "cat"], ["pots", "tops", "stop"]
    ]

    output: List[List[str]] = group_anagrams(input)

    assert sorted(output) == sorted(expected_output)
