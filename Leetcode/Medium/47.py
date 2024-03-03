from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # Hàm để sinh ra tất cả các hoán vị của tập hợp nums
        def generate_permutations(nums):
            if not nums:
                return [[]]

            result = []
            unique_permutations = set()

            for i, num in enumerate(nums):
                # Đảm bảo rằng chúng ta không tạo các hoán vị trùng lặp
                if num not in unique_permutations:
                    unique_permutations.add(num)

                    # Tạo một danh sách con bằng cách loại bỏ phần tử hiện tại
                    remaining_nums = nums[:i] + nums[i+1:]

                    # Gọi đệ quy để sinh ra tất cả các hoán vị của danh sách con
                    permutations_of_remaining = generate_permutations(remaining_nums)

                    # Kết hợp num với từng hoán vị của danh sách con
                    for perm in permutations_of_remaining:
                        result.append([num] + perm)

            return result

        return generate_permutations(nums)