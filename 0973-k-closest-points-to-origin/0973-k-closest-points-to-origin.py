class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap = []

        for x,y in points:
            distance =  x**2 + y**2
            heapq.heappush(heap, (distance, [x,y]))
        
        result = []
        for i in range(k):
            distance, coordinates = heapq.heappop(heap)
            result.append(coordinates)
        
        return result