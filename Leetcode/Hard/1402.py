from typing import List

class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        total = 0
        max_total = 0

        for s in satisfaction:
            total += s
            if total > 0:
                max_total += total
            else:
                break

        return max_total