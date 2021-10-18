from typing import List

"""
You are given a sorted array consisting of only integers where every element appears exactly twice, 
except for one element which appears exactly once. Find this single element that appears only once.

Follow up: Your solution should run in O(log n) time and O(1) space.

"""


class Solution:

    # CPU (log n) and RAM(log n)
    # you can decrease ram complexity using
    # loop instead recursion, but i am to lazy for it
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]

        def helper(l: int, r: int) -> int:
            if l >= r: return nums[l]
            m = (l + r) // 2
            if nums[m + 1] == nums[m]:
                if m % 2 == 0:
                    return helper(m, r)
                else:
                    return helper(l, m - 1)
            elif nums[m - 1] == nums[m]:
                if m % 2 == 0:
                    return helper(l, m)
                else:
                    return helper(m + 1, r)
            else:
                return nums[m]

        return helper(0, len(nums) - 1)


s = Solution()

assert 2 == s.singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]), 2
assert 10 == s.singleNonDuplicate([3, 3, 7, 7, 10, 11, 11]), 10
print("tests passed")
