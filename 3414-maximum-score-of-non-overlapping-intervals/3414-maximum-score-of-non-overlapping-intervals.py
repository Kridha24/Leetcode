from bisect import bisect_right
from typing import List


class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        intervals = sorted(
            (left, right, weight, index)
            for index, (left, right, weight) in enumerate(intervals)
        )

        n = len(intervals)
        starts = [item[0] for item in intervals]

        next_pos = [
            bisect_right(starts, intervals[i][1])
            for i in range(n)
        ]

        def insert_index(indices, value):
            """Insert value while keeping the tuple sorted."""
            position = bisect_right(indices, value)
            return indices[:position] + (value,) + indices[position:]

        previous_scores = [0] * (n + 1)
        previous_indices = [()] * (n + 1)

        for _ in range(4):
            scores = [0] * (n + 1)
            choices = [()] * (n + 1)

            for i in range(n - 1, -1, -1):
                weight = intervals[i][2]
                original_index = intervals[i][3]
                nxt = next_pos[i]

                take_score = weight + previous_scores[nxt]
                skip_score = scores[i + 1]

                if take_score > skip_score:
                    scores[i] = take_score
                    choices[i] = insert_index(
                        previous_indices[nxt],
                        original_index
                    )

                elif take_score < skip_score:
                    scores[i] = skip_score
                    choices[i] = choices[i + 1]

                else:
                    take_indices = insert_index(
                        previous_indices[nxt],
                        original_index
                    )
                    skip_indices = choices[i + 1]

                    scores[i] = take_score
                    choices[i] = min(take_indices, skip_indices)

            previous_scores = scores
            previous_indices = choices

        return list(previous_indices[0])