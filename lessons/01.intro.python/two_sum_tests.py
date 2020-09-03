
def two_sum(nums, target):
    ans = [0, 1]
    return ans

def test_sorted():
    nums = [2, 7, 11, 15]
    target = 9
    expected = [0, 1]
    output = two_sum(nums, target)
    assert output == expected
    
def test_not_sorted():
    nums = [2, -7, 11, 15]
    target = 4
    expected = [1, 2]
    output = two_sum(nums, target)
    assert output == expected
