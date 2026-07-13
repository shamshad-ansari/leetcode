class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        def dfs(adj, visited, u, v):
            visited[u] = True

            for ngbr in adj[u]:
                if ngbr == v:
                    return True
                
                if not visited[ngbr] and dfs(adj, visited, ngbr, v):
                    return True
            
            return False

        n = len(edges)
        adj = [[] for _ in range(n+1)]

        for edge in edges:
            u = edge[0]
            v = edge[1]
            visited = [False] * (n+1)
            if dfs(adj, visited, u, v):
                return edge
            
            adj[u].append(v)
            adj[v].append(u)
        
        return []