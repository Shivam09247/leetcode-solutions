class Solution:
    def minLength(self, s: str) -> int:
        lst=[]
        for i in range(len(s)):
            if (s[i]=="B" and lst and lst[-1]=="A") or (s[i]=="D" and lst and lst[-1]=="C"):
                lst.pop()

            else:
                lst.append(s[i])
        return len(lst)