class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        dic={}
        while n>0:
            a=n%10
            dic[a]=dic.get(a,0)+1
            n=n//10
        s=0
        for i in dic:
            s+=i*dic[i]
        return s

        