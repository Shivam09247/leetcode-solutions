class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=0
        l=len(digits)-1
        for i in digits:
            n+=i*(10)**l
            l-=1
        lst=[]
        n=n+1
        while n>0:
            a=n%10
            lst.append(a)
            n=n//10
        return lst[::-1]


        