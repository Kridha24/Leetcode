from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        max_factor = max(f for f, _ in items)
        freq = [0] * (max_factor + 1)
        min_price = float('inf')

        for factor, price in items:
            freq[factor] += 1
            if price < min_price:
                min_price = price

        # mult_count[f] = number of items whose factor is divisible by f
        mult_count = [0] * (max_factor + 1)
        for f in range(1, max_factor + 1):
            if freq[f] > 0:
                total = 0
                for m in range(f, max_factor + 1, f):
                    total += freq[m]
                mult_count[f] = total

        # 0/1 Knapsack for the first copy of each item
        # Value of first copy = 1 (purchased) + (mult_count[f] - 1) (free) = mult_count[f]
        dp = [0] * (budget + 1)
        for factor, price in items:
            if price > budget:
                continue
            val = mult_count[factor]
            for c in range(budget, price - 1, -1):
                if dp[c - price] + val > dp[c]:
                    dp[c] = dp[c - price] + val

        # Combine each knapsack state with greedy extra copies of the cheapest item
        ans = 0
        for c in range(budget + 1):
            extra = (budget - c) // min_price
            if dp[c] + extra > ans:
                ans = dp[c] + extra

        return ans