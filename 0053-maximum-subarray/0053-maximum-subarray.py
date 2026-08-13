class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr=nums[0]
        best=nums[0]
        def maxnum(a, b):
            if a > b:
                return a
            return b
        for i in range(1,len(nums)):
            curr=maxnum(nums[i],curr+nums[i])
            best=maxnum(best,curr)
        return best
