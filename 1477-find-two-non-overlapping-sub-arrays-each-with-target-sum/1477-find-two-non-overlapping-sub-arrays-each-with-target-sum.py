
'''
from typing import List

class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        inf = float("inf")
        best = [inf] * (n + 1)

        left = 0
        window_sum = 0
        answer = inf

        for right, value in enumerate(arr):
            window_sum += value

            while window_sum > target:
                window_sum -= arr[left]
                left += 1

            best[right + 1] = best[right]

            if window_sum == target:
                length = right - left + 1

                # best[left] uses only elements before this window.
                answer = min(answer, best[left] + length)

                best[right + 1] = min(best[right + 1], length)

        return -1 if answer == inf else answer
'''

from typing import List

class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        inf = float("inf")

        best = [inf] * (n + 1)
        seen = {0: 0}
        prefix = 0
        answer = inf

        for i, value in enumerate(arr, 1):
            prefix += value
            best[i] = best[i - 1]

            needed = prefix - target

            if needed in seen:
                start = seen[needed]
                length = i - start

                # Pair with a valid subarray entirely before start.
                answer = min(answer, best[start] + length)
                best[i] = min(best[i], length)

            seen[prefix] = i

        return -1 if answer == inf else answer
