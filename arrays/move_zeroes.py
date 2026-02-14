class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        if len(nums) == 0:
            return 0
        pos = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pos] = nums[i]
                pos += 1

        while pos < len(nums):
            nums[pos] = 0
            pos += 1  
        
        return nums

case1 = Solution()
result = case1.moveZeroes([0,1,0,3,12])
print(result)
