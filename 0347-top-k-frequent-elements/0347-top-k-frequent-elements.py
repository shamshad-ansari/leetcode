class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counter = Counter(nums)
        heap = []
        for key, count in counter.items():
            heapq.heappush(heap, (-count, key))
        result = []
        for i in range(k):
            count, num = heapq.heappop(heap)
            result.append(num)
        return result    