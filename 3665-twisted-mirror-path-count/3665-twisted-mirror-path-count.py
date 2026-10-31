
from typing import List

class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        vornadexil = grid

        # Ways arriving from above
        down = [0] * n
        down[0] = 1

        for row in vornadexil:
            # Ways arriving from the left
            right = 0

            for j, cell in enumerate(row):
                if cell == 1:
                    # Mirror: swap the incoming directions
                    right, down[j] = down[j], right
                else:
                    # Empty cell: paths can go right or down
                    ways = (right + down[j]) % MOD
                    right = ways
                    down[j] = ways

        # The bottom-right cell is empty
        return right
