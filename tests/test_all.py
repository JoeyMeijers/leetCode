import pytest
from typing import List
from two_sum import twoSum

def test_two_sum():
    # Arrange
    nums: List[int] = [1, 3, 6, 8]
    target: int = 11
    expected_result: List[int] = [1, 3]
    # Act
    result: List[int] = twoSum(nums, target)
    # Assert
    assert expected_result == result