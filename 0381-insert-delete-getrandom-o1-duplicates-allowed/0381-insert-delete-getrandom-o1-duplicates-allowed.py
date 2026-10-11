class RandomizedCollection:

    def __init__(self):
        self.RandomSet = defaultdict(set)
        self.arr = []
        

    def insert(self, val: int) -> bool:
        toReturn = False
        if val not in self.RandomSet:
            toReturn = True
        self.RandomSet[val].add(len(self.arr))
        self.arr.append(val)
        return toReturn

    def remove(self, val: int) -> bool:
        if val not in self.RandomSet:
            return False

        idx = self.RandomSet[val].pop()

        if idx != len(self.arr) - 1:
            self.RandomSet[self.arr[-1]].remove(len(self.arr) - 1)
            self.RandomSet[self.arr[-1]].add(idx)

        self.arr[idx], self.arr[-1] = self.arr[-1], self.arr[idx]
        self.arr.pop()

        if len(self.RandomSet[val]) == 0:
            self.RandomSet.pop(val)
        return True      

    def getRandom(self) -> int:
        return self.arr[random.randint(0,len(self.arr)-1)]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
