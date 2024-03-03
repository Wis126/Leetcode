from typing import List


class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        MOD = 10 ** 9 + 7
        n = len(locations)

        # Tạo mảng dp để lưu số lượng đường đi từ mỗi thành phố với mỗi lượng nhiên liệu
        dp = [[-1] * (fuel + 1) for _ in range(n)]

        def dfs(city, remaining_fuel):
            # Kiểm tra nếu giá trị đã được tính trước đó
            if dp[city][remaining_fuel] != -1:
                return dp[city][remaining_fuel]

            # Khởi tạo số lượng đường đi từ thành phố hiện tại
            routes = 0
            if city == finish:
                routes = 1

            # Thực hiện đệ quy để tính số lượng đường đi từ các thành phố kế tiếp
            for next_city in range(n):
                if next_city != city:
                    fuel_needed = abs(locations[city] - locations[next_city])
                    if remaining_fuel >= fuel_needed:
                        routes = (routes + dfs(next_city, remaining_fuel - fuel_needed)) % MOD

            # Lưu giá trị tính được vào dp và trả về
            dp[city][remaining_fuel] = routes
            return routes

        return dfs(start, fuel)