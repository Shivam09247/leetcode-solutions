class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums=sorted(nums)
        i,j=0,len(nums)-1
        avg=[]
        while i<j:
            av=(nums[i]+nums[j])/2
            i+=1
            j-=1
            avg.append(av)
        return min(avg)


        