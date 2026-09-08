class Solution:
    def countCommas(self, n: int) -> int:
        # Only numbers from 1,000 onwards contain a comma.
        return max(0, n - 999)