class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [False] * n

        def dfs(node):
            visited[node] = True
            for nei in rooms[node]:
                if not visited[nei]:
                    dfs(nei)
        
        dfs(0)
        
        return True if len(set(visited)) == 1 else False  