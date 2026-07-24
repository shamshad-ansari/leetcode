class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.components = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)

        if px == py:
            return

        if self.rank[px] > self.rank[py]:
            self.parent[py] = px
        elif self.rank[px] < self.rank[py]:
            self.parent[px] = py
        else:
            self.parent[py] = px
            self.rank[px] += 1
        
        self.components -= 1

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        dsu = DSU(n)
        
        for i in range(n):
            # Can also run till n but just duplicated effort as the upper triangle
            # covers everthing as (1,2) and (2,1) are same here (connections)
            # for j in range(n):
            for j in range(i+1, n):
                if isConnected[i][j] == 1:
                    dsu.union(i,j)
        return dsu.components