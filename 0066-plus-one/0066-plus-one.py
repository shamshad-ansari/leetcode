class Solution:
    def plusOne(self, arr: List[int]) -> List[int]:
        tmp = []
        for num in arr:
            tmp.append(str(num))
        num = int(''.join(tmp))
        num += 1
        num = str(num)
        result = []
        for n in num:
            result.append(int(n))
        return result


            