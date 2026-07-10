class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist = [float("inf")] * n
        dist[src] = 0

        for _ in range(k + 1):
            temp = dist[:]
            for u, v, price in flights:
                if dist[u] != float("inf"):
                    temp[v] = min(temp[v], dist[u] + price)
            dist = temp

        return -1 if dist[dst] == float("inf") else dist[dst]

# Can also be replace by this, just looks like dijkstra so easier to remember and engrain the concept intially
# Won't matter later as you will know how the algorithm works
        # for _ in range(k+1):
        #     temp = dist[:]
        #     for u, v, price in flights:
        #         if dist[u] == float("inf"):
        #             continue

        #         newCost = dist[u] + price

        #         if newCost < temp[v]:
        #             temp[v] = newCost
        #     dist = temp