from two_sum import twoSum
from typing import List


def test_two_sum():
    nums: List[int] = [1, 3, 6, 8]
    target: int = 11
    expected_result: List[int] = [1, 3]

    result: List[int] = twoSum(nums, target)

    assert expected_result == result
