from top_k_frequent_elements import top_k_frequent_elements


def test_top_k_frequent_elements():
    nums = [1, 2, 2, 3, 3, 3]
    k = 2
    result = top_k_frequent_elements(nums, k)
    expected = [2, 3]
    assert sorted(result) == expected
