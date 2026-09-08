class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        heap = []

        for char, c in count.items():
            heapq.heappush(heap, (-c, char))
        
        result = []
        
        while heap:
            c, char = heapq.heappop(heap)
            result.append(char * -c)
        
        return ''.join(result)