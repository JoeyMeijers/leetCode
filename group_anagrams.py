"""
Given an array of strings strs, group all anagrams together into sublists.
You may return the output in any order.

An anagram is a string that contains the exact same characters as another
string, but the order of the characters can be different.

Example 1:

Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
Example 2:

Input: strs = ["x"]

Output: [["x"]]
Example 3:

Input: strs = [""]

Output: [[""]]
Constraints:

1 <= strs.length <= 1000.
0 <= strs[i].length <= 100
strs[i] is made up of lowercase English letters.
"""


from typing import List
import string


def group_anagrams(strs: List[str]) -> List[List[str]]:
    base_key = [0] * 26
    # Create dict with all the letters and an index
    letters = {char: idx for idx, char in enumerate(string.ascii_lowercase)}
    m: dict = {}

    for word in strs:
        tmp_key = base_key.copy()
        for l in word:
            index = letters[l]
            tmp_key[index] += 1
        key = "".join(str(tmp_key))
        if key in m:
            m[key].append(word)
        else:
            m[key] = [word]

    result: List[List[str]] = []
    for k, v in m.items():
        result.append(v)
    return result
