
class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        INF = float("inf")

        # Step 1: Precompute the cost of every substring
        cost = [[INF] * n for _ in range(n)]

        for i in range(n):
            for j in range(i + 1, n):
                length = j - i + 1

                for d in range(1, length):
                    if length % d != 0:
                        continue

                    group_len = length // d
                    changes = 0

                    # Each group must be a palindrome
                    for r in range(d):
                        for p in range(group_len // 2):
                            left = i + r + p * d
                            right = i + r + (group_len - 1 - p) * d

                            if s[left] != s[right]:
                                changes += 1

                    cost[i][j] = min(cost[i][j], changes)

        # Step 2: DP for exactly k substrings
        dp = [[INF] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for parts in range(1, k + 1):
            for i in range(2 * parts, n + 1):
                # Last substring is s[t:i]
                for t in range(2 * (parts - 1), i - 1):
                    dp[i][parts] = min(
                        dp[i][parts],
                        dp[t][parts - 1] + cost[t][i - 1]
                    )

        return dp[n][k]
