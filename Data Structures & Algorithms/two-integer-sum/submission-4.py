class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #first = 0
        #second = 1

        for first in range(len(nums)):
            for second in range(first + 1, len(nums)):
                if nums[first] + nums[second] == target:
                    return [first, second]

        #return [-1]