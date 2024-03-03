from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        # Sử dụng vòng lặp để trộn mảng theo yêu cầu
        for i in range(n):
            # Thêm phần tử x_i vào mảng kết quả
            result.append(nums[i])
            # Thêm phần tử y_i vào mảng kết quả
            result.append(nums[i + n])
        return result