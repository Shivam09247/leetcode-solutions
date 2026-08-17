class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        def prime(x):
            if x<2:
                return False
            for i in range(2,int(x**0.5)+1):
                if x%i==0:
                    return False
            return True
        dic={}
        for i in nums:
            dic[i]=dic.get(i,0)+1
        for i in dic:
            if prime(dic[i])==True:
                return True
        return False