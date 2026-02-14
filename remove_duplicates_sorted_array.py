class Solution:
    def removeDuplicates(self, arr: List[int]) -> int:
        if len(arr) == 0:
            return 0

        pos = 0
        for i in range(1,len(arr)):
            if arr[i] != arr[pos]:
                pos += 1
                arr[pos] = arr[i]

        return pos +1

case1 = Solution()
arr = [1,3,3,5,5,5,6,7,7]
k = case1.removeDuplicates(arr)
print(arr[:k])
        
