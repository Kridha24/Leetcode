from typing import List

class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)

        min_index = nums.index(min(nums))
        max_index = nums.index(max(nums))

        left = min(min_index, max_index)
        right = max(min_index, max_index)

        # Three possible strategies
        front_only = right + 1
        back_only = n - left
        both_sides = (left + 1) + (n - right)

        return min(front_only, back_only, both_sides)