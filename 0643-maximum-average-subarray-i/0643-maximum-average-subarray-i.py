class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        subsum=sum(nums[:k])
        maxsum=subsum
        for j in range(k,len(nums)):
            subsum+=nums[j]
            subsum-=nums[j-k]
            if subsum>maxsum:
                maxsum=subsum
        return maxsum/k

        