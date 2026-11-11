
class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int,
                    need1: int, need2: int) -> int:

        both = min(need1, need2)

        option1 = both * min(costBoth, cost1 + cost2)
        option2 = (need1 - both) * min(cost1, costBoth)
        option3 = (need2 - both) * min(cost2, costBoth)

        return option1 + option2 + option3
