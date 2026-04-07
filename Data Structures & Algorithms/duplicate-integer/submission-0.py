class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        frequency_dict = {}

        for elem in nums:
            if elem in frequency_dict.keys():
                frequency_dict[elem] += 1
                return True
            else:
                frequency_dict[elem] = 0
        
        return False