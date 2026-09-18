from typing import List

class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        first = {}
        last = {}

        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i

        intervals = []

        for ch, left in first.items():
            right = last[ch]
            i = left

            while i <= right:
                current = s[i]

                # This character has an occurrence outside the left edge.
                if first[current] < left:
                    break

                # Include all occurrences of this character.
                right = max(right, last[current])
                i += 1
            else:
                intervals.append((left, right))

        # Prefer earlier endings; for ties, prefer shorter intervals.
        intervals.sort(key=lambda interval: (interval[1], -interval[0]))

        answer = []
        previous_end = -1

        for left, right in intervals:
            if left > previous_end:
                answer.append(s[left:right + 1])
                previous_end = right

        return answer