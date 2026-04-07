class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        # brute force O(n^3)
        if len(nums) < 3:
            return []
        
        nums.sort()

        res = set()

        for a in range(len(nums)):
            for b in range(a + 1, len(nums)):
                for c in range(b + 1, len(nums)):
                    if nums[a] + nums[b] + nums[c] == 0:
                        res.add((nums[a], nums[b], nums[c]))
        
        return [list(i) for i in res]
        """
        """
        if len(nums) < 3:
            return []
        
        nums.sort()
        res = set()
        l = 0
        r = len(nums) - 1
        m = (l + r) // 2

        while l < m and r > m:
            tot = nums[l] + nums[m] + nums[r]
            if tot == 0:
                res.add((nums[l] + nums[m] + nums[r]))
            elif tot > 0:
                r -= 1
            else:
                l += 1
        return [list(i) for i in res]
        """
        if len(nums) < 3:
            return []

        nums.sort()
        res = set()
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                target = -nums[i]
                if nums[j] + nums[k] == target:
                    res.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif nums[j] + nums[k] < target:
                    j += 1
                else:
                    k -= 1
        return [list(i) for i in res]

