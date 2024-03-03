from sortedcontainers import SortedList

class Solution:
    def countOperationsToEmptyArray(self, nums: List[int]) -> int:
        N = len(nums)
        sl = SortedList()

        for i in range(N):
            sl.add(i)

        heap = [(num, i) for i, num in enumerate(nums)]
        heapq.heapify(heap)

        prev = 0
        result = 0
        while heap:
            _, i = heapq.heappop(heap)
            delta = sl.bisect_left(i) - sl.bisect_left(prev)
            result += delta % len(sl)
            sl.discard(i)
            prev = i

        return result + N