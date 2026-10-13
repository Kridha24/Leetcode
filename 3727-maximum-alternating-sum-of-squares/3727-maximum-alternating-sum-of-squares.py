'''
class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        squares = sorted(x * x for x in nums)

        n = len(squares)
        negative_count = n // 2

        score = 0

        for i in range(n):
            if i < negative_count:
                score -= squares[i]
            else:
                score += squares[i]

        return score
'''

import numpy as np

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        # n = len(nums)
        # nums = sorted(map(abs, nums))
        # return sum(x * x for x in nums[n//2:]) - sum(x * x for x in nums[:n//2])

        sq = np.square(np.array(nums, dtype=np.int64))
        h = len(nums) // 2
        return int(sq.sum() - 2 * np.partition(sq, h)[:h].sum())  # smallest h squares moved to the front, O(n)
    