class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t)>len(s):
            s,t=t,s
        dic={}
        for i in s:
            dic[i]=dic.get(i,0)+1
        dic2={}
        for i in t:
            dic2[i]=dic2.get(i,0)+1
        for i in dic:
            if i not in dic2 or dic[i]!=dic2[i]:
                return False
        return True
        