class Solution:
    def mostFrequentEven(self, nums: list[int]) -> int:
        dic={}
        for i in nums:
            if i%2==0:
                dic[i]=dic.get(i,0)+1
        v=float(inf)
        ma=float(-inf)
        for i in dic:
            if dic[i]==ma:
                v=min(i,v)
            elif dic[i]>ma:
                ma=dic[i]
                v=i
        return v if v!=float(inf) else -1

        