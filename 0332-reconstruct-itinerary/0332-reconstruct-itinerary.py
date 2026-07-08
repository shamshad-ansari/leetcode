class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for v,u in tickets:
            graph[v].append(u)
        
        for key in graph:
            graph[key].sort(reverse=True)

        result = []
        
        def dfs(node):
            while graph[node]:
                nxt = graph[node].pop()
                dfs(nxt)
            result.append(node)
        
        dfs("JFK")
        return result[::-1]