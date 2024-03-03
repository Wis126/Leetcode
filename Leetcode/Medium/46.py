from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start):
            if start == len(nums) - 1:
                result.append(nums[:])  # Sao chép hoán vị hiện tại vào danh sách kết quả
                return

            for i in range(start, len(nums)):
                # Hoán đổi các phần tử để tạo ra các hoán vị
                nums[start], nums[i] = nums[i], nums[start]

                # Đệ quy để tạo ra các hoán vị cho các phần tử còn lại
                backtrack(start + 1)

                # Backtrack bằng cách hoàn ngược lại việc hoán đổi
                nums[start], nums[i] = nums[i], nums[start]

        result = []
        backtrack(0)
        return result