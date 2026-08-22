class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic={}
        for i in magazine:
            dic[i]=dic.get(i,0)+1
        for i in ransomNote:
            if i not in dic or dic[i]==0:
                return False
            dic[i]-=1
        return True

        