from typing import List

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # dp[j] will store a set of all possible XOR sums to reach column j in the current row
        dp = [set() for _ in range(n)]
        dp[0].add(grid[0][0])
        
        for i in range(m):
            for j in range(n):
                # Skip the starting cell as it's already initialized
                if i == 0 and j == 0:
                    continue
                
                val = grid[i][j]
                
                # Fetch sets from the top cell (if valid)
                new_set = {x ^ val for x in dp[j]} if i > 0 else set()
                
                # Fetch and add sets from the left cell (if valid)
                if j > 0:
                    new_set.update(x ^ val for x in dp[j-1])
                
                # Overwrite the DP state for the current column
                dp[j] = new_set
                
        # Return the minimum possible XOR sum at the bottom-right corner
        return min(dp[-1])