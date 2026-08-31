class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        a=s1.split()
        lst=[]
        b=s2.split()
        dic1={}
        for i in a:
            dic1[i]=dic1.get(i,0)+1
        dic2={}
        for i in b:
            dic2[i]=dic2.get(i,0)+1
        for i in dic1:
            if dic1[i]==1 and i not in dic2:
                lst.append(i)
        for i in dic2:
            if dic2[i]==1 and i not in dic1:
                lst.append(i)
        return lst