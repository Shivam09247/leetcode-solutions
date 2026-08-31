class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        lst=[]
        s=""
        for i in paragraph:
            if 97<=ord(i.lower())<=122:
                s+=i
            else:
                if s:
                    lst.append(s.lower())
                s=""
        lst.append(s.lower())
        dic={}
        for i in lst:
            dic[i]=dic.get(i,0)+1
        ma=float("-inf")
        v=""
        for i in dic:
            if i not in banned:
                if dic[i]>ma:
                    ma=dic[i]
                    v=i
        return v


