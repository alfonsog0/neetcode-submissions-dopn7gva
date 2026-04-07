class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #for first in range(len(nums)):
            #for second in range(first + 1, len(nums)):
                #if nums[first] + nums[second] == target:
                    #return [first, second]

        #return [-1]
        hash_map = {}

        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in hash_map:
                return [hash_map[difference], i]
            else:
                hash_map[nums[i]] = i 
