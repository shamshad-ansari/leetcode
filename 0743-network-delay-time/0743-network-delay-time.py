class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for u, v, w in times:
            adj[u].append([v, w])
        
        dist = [float('inf')] * (n+1)
        dist[k] = 0
        q = [(0,k)]

        while q:
            weight, curr = heapq.heappop(q)

            if dist[curr] < weight:
                continue
            
            for v, w in adj[curr]:
                cw = weight + w
                if cw < dist[v]:
                    dist[v] = cw
                    heapq.heappush(q, (cw, v))

        dist = dist[1:]
        return max(dist) if max(dist)!= float('inf') else -1