from typing import List
from math import gcd

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:

        coins.sort()

        # Remove redundant coins
        useful = []
        for c in coins:
            if not any(c % x == 0 for x in useful):
                useful.append(c)

        coins = useful
        n = len(coins)

        def lcm(a, b):
            return a // gcd(a, b) * b

        # Count valid amounts <= x
        def count(x):
            ans = 0

            # Inclusion-Exclusion
            for mask in range(1, 1 << n):
                multiple = 1
                bits = 0

                for i in range(n):
                    if mask & (1 << i):
                        bits += 1
                        multiple = lcm(multiple, coins[i])

                        if multiple > x:
                            break

                else:
                    if bits % 2 == 1:
                        ans += x // multiple
                    else:
                        ans -= x // multiple

            return ans

        # Binary Search
        left = 1
        right = min(coins) * k

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left