class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        s_nums1 = set(nums1)
        s_nums2 = set(nums2)
        only1 = s_nums1 - s_nums2
        only2 = s_nums2 - s_nums1
        return [list(only1), list(only2)]      