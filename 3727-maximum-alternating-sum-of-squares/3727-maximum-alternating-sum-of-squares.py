
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
