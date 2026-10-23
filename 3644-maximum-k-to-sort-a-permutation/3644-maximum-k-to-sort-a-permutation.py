from typing import List

class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        and_sum = -1

        for i, val in enumerate(nums):
            if i != val:
                and_sum &= val
                
        return 0 if and_sum == -1 else and_sum
        