class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = [False] * n

        adj = [[] for _ in range(n)]

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)

                adj[i].append((j, dist))
                adj[j].append((i, dist))

        total = 0
        visited_count = 0
        pq = [(0, 0)]          # (weight, node)

        while pq:
            wt, node = heapq.heappop(pq)

            if visited[node]:
                continue

            visited[node] = True
            total += wt
            visited_count += 1

            if visited_count == n:
                break

            for neighbor, edge_wt in adj[node]:
                if not visited[neighbor]:
                    heapq.heappush(pq, (edge_wt, neighbor))

        return total