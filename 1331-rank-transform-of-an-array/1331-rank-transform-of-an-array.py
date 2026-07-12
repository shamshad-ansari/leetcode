class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # can take set of sorted array. Give O(klogk) still O(nlogn) in worst case but
        # better average case. However, I'm lazy so I'll leave it like this
        if not arr:
            return []
            
        temp = sorted(arr)
        mp = {}
        rank = 1
        prev = temp[0]

        for i in range(len(arr)):
            if prev != temp[i]:
                rank += 1
            prev = temp[i]
            mp[temp[i]] = rank
        
        for i in range(len(arr)):
            arr[i] = mp[arr[i]]
        
        return arr