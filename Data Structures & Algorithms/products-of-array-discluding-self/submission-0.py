class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mult = 1
        zeros = 0
        zero_index = -1

        for idx, num in enumerate(nums):
            if num == 0:
                zeros += 1
                zero_index = idx
            else:
                mult *= num
        
        if zeros > 1:
            return [0] * len(nums)
        
        output = []
        for num in nums:
            if zeros:
                if num:
                    output.append(0)
                else:
                    output.append(mult)
            else:
                output.append(int(mult/num))
        return output
