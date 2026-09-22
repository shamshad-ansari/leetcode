class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        if key in self.store:
            arr = self.store[key]
            n = len(arr)
            val, time = self.binarySearch(0, n-1, arr, timestamp)
            if time <= timestamp:
                return val
        return ''

    def binarySearch(self, start, end, arr, timestamp):
        best = arr[0]
        while start <= end:
            mid = (start+end)//2
            if arr[mid][1] == timestamp:
                return arr[mid]
            elif arr[mid][1] < timestamp:
                start = mid + 1
                best = arr[mid]
            else:
                end = mid-1
        return best
            



        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)