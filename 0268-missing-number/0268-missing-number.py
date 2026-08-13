class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        miss=n
        for i,j in enumerate(nums):
            miss^=i^j
        return miss
        