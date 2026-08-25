class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        st=""
        w=""
        l=0
        for i in s:
            if i!=" ":
                w+=i
            else:
                if w:
                    st+=w
                    l+=1
                    if l==k:
                        break
                w=""
                st+=i
        if l<k:
            st+=w
        return st


