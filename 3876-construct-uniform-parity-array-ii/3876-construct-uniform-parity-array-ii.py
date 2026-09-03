from typing import List

class Solution:
    def uniformArray(self, nums1: List[int]) -> bool:
        minimum = min(nums1)

        if minimum % 2 == 1:
            return True

        return all(num % 2 == 0 for num in nums1)