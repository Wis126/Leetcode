from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))

        def custom_compare(x, y):
            return int(x + y) - int(y + x)

        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if custom_compare(nums[j], nums[i]) > 0:
                    nums[i], nums[j] = nums[j], nums[i]

        result = ''.join(nums)

        return str(int(result))