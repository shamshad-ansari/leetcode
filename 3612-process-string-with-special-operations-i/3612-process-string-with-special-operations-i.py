class Solution:
    def processStr(self, s: str) -> str:
        result = []
        for letter in s:
            if letter == '*':
                if result:
                    result.pop()
            elif letter == '#':
                result += result.copy()
            elif letter == '%':
                result.reverse()
            else:
                result.append(letter)
        return ''.join(result)
        