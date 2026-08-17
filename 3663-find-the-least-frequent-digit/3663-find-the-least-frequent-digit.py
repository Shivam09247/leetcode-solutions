class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        dic={}
        while n>0:
            a=n%10
            dic[a]=dic.get(a,0)+1
            n=n//10
        ele=0
        mi=float("inf")
        for i,j in dic.items():
            if j==mi:
                if i<ele:
                    ele=i
                    mi=j
            if j<mi:
                mi=j
                ele=i
        return ele

