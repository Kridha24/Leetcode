from typing import List

class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        path_length = m + n - 1

        if (path_length % 2 != 0
                or grid[0][0] == ')'
                or grid[-1][-1] == '('):
            return False

        # dp[j]: possible balances after visiting column j.
        dp = [set() for _ in range(n)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    previous = {0}
                else:
                    previous = set(dp[j])  # From above

                    if j > 0:
                        previous.update(dp[j - 1])  # From left

                change = 1 if grid[i][j] == '(' else -1
                remaining = (m - 1 - i) + (n - 1 - j)

                dp[j] = {
                    balance + change
                    for balance in previous
                    if 0 <= balance + change <= remaining
                }

        return 0 in dp[-1]