class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        dic={}
        for i in nums:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        su=0
        for i in dic:
            if dic[i]%k==0:
                su+=i*dic[i]
        return su
        