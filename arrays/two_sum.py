class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            need = target - nums[i]

            if need in seen:
                return [seen[need],i]

            seen[nums[i]] = i

case1 = Solution()
result = case1.twoSum([2,7,11,15],9)
print(result)  
