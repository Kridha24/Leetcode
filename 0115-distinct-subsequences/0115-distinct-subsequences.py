class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(t)

        if m > len(s):
            return 0

        # dp[j] = ways to create t[:j] using processed characters of s
        dp = [0] * (m + 1)
        dp[0] = 1  # Empty string can always be created once

        for char in s:
            # Reverse traversal prevents using the same character twice
            for j in range(m, 0, -1):
                if char == t[j - 1]:
                    dp[j] += dp[j - 1]

        return dp[m]