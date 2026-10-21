import heapq

class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        m = len(heights)
        n = len(heights[0])
        q = [(0, 0, 0)]

        dist = []
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]

        for i in range(m):
            dist.append([float('inf')] * n)

        dist[0][0] = 0

        while q:
            d, r, c = heapq.heappop(q)

            if d > dist[r][c]:
                continue

            if r == m - 1 and c == n - 1:
                return d

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if not (0 <= nr < m and 0 <= nc < n):
                    continue

                new_w = max(d, abs(heights[nr][nc] - heights[r][c]))

                if new_w < dist[nr][nc]:
                    dist[nr][nc] = new_w
                    heapq.heappush(q, (new_w, nr, nc))