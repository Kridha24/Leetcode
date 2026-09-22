from typing import List

class Solution:
    def resultArray(
        self, nums: List[int], k: int, queries: List[List[int]]
    ) -> List[int]:
        n = len(nums)
        size = 1
        while size < n:
            size *= 2

        # Empty interval: multiplicative identity, no non-empty prefixes.
        identity = (1 % k, [0] * k)
        tree = [identity] * (2 * size)

        def merge(left, right):
            left_product, left_counts = left
            right_product, right_counts = right

            counts = left_counts.copy()

            for remainder in range(k):
                combined = (left_product * remainder) % k
                counts[combined] += right_counts[remainder]

            product = (left_product * right_product) % k
            return product, counts

        def make_leaf(value):
            remainder = value % k
            counts = [0] * k
            counts[remainder] = 1
            return remainder, counts

        # Build the tree.
        for i, value in enumerate(nums):
            tree[size + i] = make_leaf(value)

        for node in range(size - 1, 0, -1):
            tree[node] = merge(tree[2 * node], tree[2 * node + 1])

        result = []

        for index, value, start, x in queries:
            # Apply the persistent point update.
            node = size + index
            tree[node] = make_leaf(value)
            node //= 2

            while node:
                tree[node] = merge(tree[2 * node], tree[2 * node + 1])
                node //= 2

            # Query the interval [start, n).
            left = size + start
            right = size + n
            left_result = identity
            right_result = identity

            while left < right:
                if left & 1:
                    left_result = merge(left_result, tree[left])
                    left += 1

                if right & 1:
                    right -= 1
                    right_result = merge(tree[right], right_result)

                left //= 2
                right //= 2

            _, counts = merge(left_result, right_result)
            result.append(counts[x])

        return result