class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        n = len(passingFees)
        adj = [[] for _ in range(n)]
        minFee = [
                    [math.inf] * (maxTime + 1)
                    for _ in range(n)
                ]
                
        minFee[0][0] = passingFees[0]

        for u, v, t in edges:
            adj[u].append((v, t))
            adj[v].append((u, t))

        pq = [(passingFees[0], 0, 0)]

        while pq:
            fee, time, node = heapq.heappop(pq)

            if minFee[node][time] < fee:
                continue
            
            if node == n - 1:
                return fee

            
            for nei, travelTime in adj[node]:
                new_time = time + travelTime

                if new_time > maxTime:
                    continue
                
                new_fee = fee + passingFees[nei]

                if new_fee < minFee[nei][new_time]:
                    minFee[nei][new_time] = new_fee
                    heapq.heappush(pq, (new_fee, new_time, nei))

        return -1