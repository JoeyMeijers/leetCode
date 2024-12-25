"""
Given two strings s and t, return true if the two strings are anagrams of
each other, otherwise return false.

A anagram is a string that contains the exact same characters as
another string, but the order of the characters can be different.

Example 1:

Input: s = "racecar", t = "carrace"

Output: true
Example 2:

Input: s = "jar", t = "jam"

Output: false
Constraints:

s and t consist of lowercase English letters.
"""


def valid_anagram(s1: str, s2: str) -> bool:
    m: dict = {}

    for l in s1:
        if l in m:
            m[l] += 1
        else:
            m[l] = 1

    for l in s2:
        if l not in m:
            return False
        m[l] -= 1

    for k, v in m.items():
        if v != 0:
            return False

    return True
