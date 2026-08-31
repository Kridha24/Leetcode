# Definition for singly-linked list:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        first_critical = -1
        previous_critical = -1
        min_distance = float("inf")

        previous = head
        current = head.next
        position = 1  # 0-indexed position of current node

        while current.next:
            is_maximum = (
                current.val > previous.val
                and current.val > current.next.val
            )
            is_minimum = (
                current.val < previous.val
                and current.val < current.next.val
            )

            if is_maximum or is_minimum:
                if first_critical == -1:
                    first_critical = position
                else:
                    min_distance = min(
                        min_distance,
                        position - previous_critical
                    )

                previous_critical = position

            previous = current
            current = current.next
            position += 1

        # Fewer than two critical points
        if min_distance == float("inf"):
            return [-1, -1]

        max_distance = previous_critical - first_critical
        return [min_distance, max_distance]