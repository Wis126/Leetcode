from typing import List

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        target_mask = (1 << n) - 1  # Sử dụng bit mask để theo dõi việc đã ghé thăm tất cả các nút chưa

        queue = []
        visited = set()

        # Mỗi state trong queue sẽ là một tuple (node, mask, steps)
        # node: nút hiện tại, mask: bit mask để kiểm tra đã ghé thăm tất cả các nút chưa, steps: số bước đã đi
        for i in range(n):
            queue.append((i, 1 << i, 0))
            visited.add((i, 1 << i))

        while queue:
            node, mask, steps = queue[0]
            del queue[0]  # Xóa phần tử đầu tiên khỏi danh sách

            if mask == target_mask:
                return steps  # Nếu đã ghé thăm tất cả các nút, trả về số bước đã đi

            for neighbor in graph[node]:
                # Dùng bit mask để kiểm tra xem nút neighbor đã được ghé thăm chưa
                neighbor_mask = mask | (1 << neighbor)

                # Nếu chưa ghé thăm nút neighbor với mask mới, thêm nút và mask vào queue
                if (neighbor, neighbor_mask) not in visited:
                    queue.append((neighbor, neighbor_mask, steps + 1))
                    visited.add((neighbor, neighbor_mask))

        return -1  # Nếu không tìm thấy đường đi thỏa mãn