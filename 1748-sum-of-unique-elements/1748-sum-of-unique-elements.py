class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        dic={}
        s=0
        for i in nums:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1

        for i  in dic:
            if dic[i]==1:
                s+=i
        return s

        