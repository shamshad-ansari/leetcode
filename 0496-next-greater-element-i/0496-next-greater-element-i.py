class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        map = {}
        stk = []

        for i in range(len(nums2)-1,-1,-1):
            curr = nums2[i]
            while stk and stk[-1] <= curr:
                stk.pop()
            if not stk:
                map[curr] = -1
            else:
                map[curr] = stk[-1]
            stk.append(curr)
        
        result = [0] * len(nums1)

        for i in range(len(nums1)):
            curr = nums1[i]
            result[i] = map[curr]
        
        return result  