from bisect import bisect_right
from functools import lru_cache
from typing import List

class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2.sort()
        n = len(arr1)
        inf = float('inf')

        @lru_cache(None)
        def dp(i, prev):
            if i == n:
                return 0
            ans = inf
            if arr1[i] > prev:
                ans = min(ans, dp(i + 1, arr1[i]))
            loc = bisect_right(arr2, prev)
            if loc < len(arr2):
                ans = min(ans, 1 + dp(i + 1, arr2[loc]))
            return ans

        res = dp(0, -inf)
        return res if res != inf else -1