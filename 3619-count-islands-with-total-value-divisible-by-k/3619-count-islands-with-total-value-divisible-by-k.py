
class Solution:
    def countIslands(self, grid: list[list[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    stack = [(i, j)]
                    total = 0

                    while stack:
                        r, c = stack.pop()

                        if (r < 0 or r >= m or
                            c < 0 or c >= n or
                            grid[r][c] == 0):
                            continue

                        total += grid[r][c]
                        grid[r][c] = 0  # Mark visited

                        stack.append((r + 1, c))
                        stack.append((r - 1, c))
                        stack.append((r, c + 1))
                        stack.append((r, c - 1))

                    if total % k == 0:
                        count += 1

        return count
