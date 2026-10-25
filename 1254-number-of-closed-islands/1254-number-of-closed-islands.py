from collections import deque
from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        """
        Returns the number of closed islands (0s completely surrounded by 1s).
        
        Approach: Flood Fill (DFS / BFS)
        1. Any 0 connected to the grid boundary cannot be part of a closed island.
           First, flood-fill all boundary-connected 0s into 1s.
        2. Iterate through the remaining grid; each unvisited 0 starts a new closed
           island. Flood-fill that island to mark its cells as visited (1) and
           increment the count.
           
        Time Complexity: O(R * C) where R is rows and C is columns.
        Space Complexity: O(R * C) in the worst case for the BFS queue / recursion stack.
        """
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])

        def bfs(start_r: int, start_c: int) -> None:
            queue = deque([(start_r, start_c)])
            grid[start_r][start_c] = 1
            while queue:
                r, c = queue.popleft()
                for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                        grid[nr][nc] = 1
                        queue.append((nr, nc))

        # Step 1: Flood-fill all land (0) connected to the boundaries
        for r in range(rows):
            for c in (0, cols - 1):
                if grid[r][c] == 0:
                    bfs(r, c)

        for c in range(cols):
            for r in (0, rows - 1):
                if grid[r][c] == 0:
                    bfs(r, c)

        # Step 2: Count and flood-fill remaining closed islands
        closed_islands = 0
        for r in range(1, rows - 1):
            for c in range(1, cols - 1):
                if grid[r][c] == 0:
                    closed_islands += 1
                    bfs(r, c)

        return closed_islands


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    grid1 = [
        [1, 1, 1, 1, 1, 1, 1, 0],
        [1, 0, 0, 0, 0, 1, 1, 0],
        [1, 0, 1, 0, 1, 1, 1, 0],
        [1, 0, 0, 0, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 0],
    ]
    assert sol.closedIsland(grid1) == 2, "Example 1 failed"

    # Example 2
    grid2 = [
        [0, 0, 1, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 1, 1, 1, 0],
    ]
    assert sol.closedIsland(grid2) == 1, "Example 2 failed"

    # Example 3
    grid3 = [
        [1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1],
    ]
    assert sol.closedIsland(grid3) == 2, "Example 3 failed"

    print("All example tests passed!")