from typing import List


class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        min_price = min(price for _, price in items)

        cnt = [0] * (n + 1)
        for factor, _ in items:
            cnt[factor] += 1

        mult_cnt = [0] * (n + 1)
        for f in range(1, n + 1):
            if cnt[f] == 0:
                continue
            total = 0
            for m in range(f, n + 1, f):
                total += cnt[m]
            mult_cnt[f] = total

        items_sorted = sorted(items, key=lambda x: x[1])
        ans = 0

        for factor, price in items_sorted:
            if price >= 2 * min_price or budget < price:
                break
            d = mult_cnt[factor] - 1
            if d <= 0:
                continue
            take = min(d, budget // price)
            ans += 2 * take
            budget -= take * price

        ans += budget // min_price
        return ans