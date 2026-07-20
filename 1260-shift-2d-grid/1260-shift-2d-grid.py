from typing import List

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:

        # Number of rows
        m = len(grid)

        # Number of columns
        n = len(grid[0])

        # Total number of elements
        total = m * n

        # Reduce unnecessary shifts
        k = k % total

        # Create answer grid
        ans = [[0] * n for _ in range(m)]

        # Traverse every element
        for i in range(m):
            for j in range(n):

                # Convert 2D index to 1D index
                oldIndex = i * n + j

                # Find new position after k shifts
                newIndex = (oldIndex + k) % total

                # Convert 1D index back to 2D
                newRow = newIndex // n
                newCol = newIndex % n

                # Place the element
                ans[newRow][newCol] = grid[i][j]

        return ans