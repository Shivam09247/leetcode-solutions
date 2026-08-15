class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        dic={}
        for i in nums:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        ma=float("-inf")
        for i in dic:
            if dic[i]>ma:
                ma=dic[i]
        su=0
        for i in dic:
            if dic[i]==ma:
                su+=dic[i]
        return su
        