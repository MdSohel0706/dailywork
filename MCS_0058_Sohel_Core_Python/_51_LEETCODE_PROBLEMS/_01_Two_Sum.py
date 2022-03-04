class Solution:

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        l = len(nums)
        i = 0
        while(i < (l-1)):
            j = i+1
            while(j < l):
                if(nums[i] + nums[j] == target):
                    return [i,j]
                j += 1
            i += 1

ob = Solution()
print(ob.twoSum([2,5,5,11],10))