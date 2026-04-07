class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1

        nums.sort()

        current = 1
        longest = 1

        for i in range(1, len(nums)):
            if nums[i] == (nums[i-1] + 1):
                current += 1
            elif nums[i] == nums[i-1]:
                continue
            else:
                longest = max(current, longest)
                current = 1
        
        longest = max(current, longest)
        return longest
        """
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if num - 1 not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
