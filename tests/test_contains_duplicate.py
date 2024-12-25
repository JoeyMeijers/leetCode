from contains_duplicate import contains_duplicate
from typing import List


def test_contains_duplicate():
    input_true: List[int] = [1, 2, 3, 1]
    input_false: List[int] = [1, 2, 3, 4]

    assert contains_duplicate(input_true)
    assert not contains_duplicate(input_false)
