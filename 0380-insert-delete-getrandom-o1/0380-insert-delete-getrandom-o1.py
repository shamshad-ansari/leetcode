class RandomizedSet:

    def __init__(self):
        self.RandomizeSet = {}
        self.arr = []
        

    def insert(self, val: int) -> bool:
        if val in self.RandomizeSet:
            return False
        self.RandomizeSet[val] = len(self.arr)
        self.arr.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.RandomizeSet:
            return False
        idx = self.RandomizeSet[val]
        last_element = self.arr[-1]
        self.RandomizeSet[last_element] = idx
        self.arr[idx], self.arr[-1] = self.arr[-1], self.arr[idx]
        self.arr.pop()
        self.RandomizeSet.pop(val)
        return True
        

    def getRandom(self) -> int:
        return self.arr[random.randint(0,len(self.arr)-1)]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()