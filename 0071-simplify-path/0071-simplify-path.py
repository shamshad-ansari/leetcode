class Solution:
    def simplifyPath(self, path: str) -> str:
        tokens = [token for token in path.split('/') if token]
        stack = []
        for token in tokens:
            if stack and token == '..':
                stack.pop()
            elif token != '.' and token != '..':
                stack.append(token)
        res = []
        res.append('/')
        for p in stack:
            res.append(p)
            res.append('/')

        if len(res) == 1:
            return '/'
        return ''.join(res[:-1])