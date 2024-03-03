from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sắp xếp mảng để dễ dàng thực hiện tìm kiếm hai con trỏ
        nums.sort()

        result = []
        n = len(nums)

        for i in range(n - 2):
            # Bỏ qua trường hợp trùng lặp ở phần tử nums[i]
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, n - 1

            while left < right:
                total_sum = nums[i] + nums[left] + nums[right]

                if total_sum < 0:
                    left += 1
                elif total_sum > 0:
                    right -= 1
                else:
                    # Thêm bộ ba vào kết quả
                    result.append([nums[i], nums[left], nums[right]])

                    # Bỏ qua trường hợp trùng lặp ở phần tử nums[left]
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    # Bỏ qua trường hợp trùng lặp ở phần tử nums[right]
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Di chuyển con trỏ
                    left += 1
                    right -= 1

        return result