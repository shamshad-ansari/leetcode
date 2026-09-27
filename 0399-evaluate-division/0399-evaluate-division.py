class Solution:
    def calcEquation(self, equations, values, queries):

        def dfs(u, target, product, visited):
            if u == target:
                return product

            visited.add(u)

            for v, val in graph[u]:
                if v not in visited:
                    result = dfs(v, target, product * val, visited)

                    if result != -1.0:
                        return result

            return -1.0
        
        graph = defaultdict(list)

        for i in range(len(equations)):
            a, b = equations[i]
            val = values[i]

            graph[a].append((b, val))
            graph[b].append((a, 1 / val))

        result = []

        for dividend, divisor in queries:

            if dividend not in graph or divisor not in graph:
                result.append(-1.0)

            elif dividend == divisor:
                result.append(1.0)

            else:
                visited = set()
                val = dfs(dividend, divisor, 1.0, visited)
                result.append(val)

        return result