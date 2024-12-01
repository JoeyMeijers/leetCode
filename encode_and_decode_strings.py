"""
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode

Example 1:

Input: ["neet","code","love","you"]

Output:["neet","code","love","you"]
Example 2:

Input: ["we","say",":","yes"]

Output: ["we","say",":","yes"]
Constraints:

0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains only UTF-8 characters.
"""


from typing import List


def encode(strs: List[str]) -> str:
    result = ""
    for word in strs:
        n = len(word)
        result += str(n) + "#" + word
    return result


def decode(string: str) -> List[str]:
    res, i = [], 0

    while i < len(string):
        j = i
        while string[j] != "#":
            j += 1
        length = string[i:j]
        length = int(length)
        res.append(string[j+1: j + 1 + length])
        i = j + 1 + length
    return res


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
print("yaay")
