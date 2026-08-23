class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        dic={}
        for i in s:
            dic[i]=dic.get(i,0)+1
        a=set([i for i in dic.values()])
        return len(a)==1
        