class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        n = len(name)
        m = len(typed)

        if m < n:
            return False

        if name[0] != typed[0]:
            return False

        i = 0
        j = 0

        while i < n and j < m:

            while i < n and j < m and name[i] == typed[j]:
                i += 1
                j += 1

            while j < m and j > 0 and typed[j] == typed[j - 1]:
                j += 1

            if i < n and j < m and name[i] != typed[j]:
                return False

        return i == n and j == m