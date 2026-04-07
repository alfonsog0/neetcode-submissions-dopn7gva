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
        if len(nums) < 3:
            return []

        nums.sort()
        #res = set()
        res = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                target = -nums[i]
                if nums[j] + nums[k] == target:
                    #res.add((nums[i], nums[j], nums[k]))
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while k > j and nums[k] == nums[k+1]:
                        k -= 1
                elif nums[j] + nums[k] < target:
                    j += 1
                else:
                    k -= 1
    
        #return [list(i) for i in res]
        return res
