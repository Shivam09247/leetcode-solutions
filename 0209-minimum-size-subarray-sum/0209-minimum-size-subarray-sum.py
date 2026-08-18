class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        su=0
        mi=float("inf")
        for right in range(len(nums)):
            su+=nums[right]
            while su>=target:
                a=right-left+1
                if a<mi:
                    mi=a
                su-=nums[left]
                left+=1
        return 0 if mi==float("inf") else mi