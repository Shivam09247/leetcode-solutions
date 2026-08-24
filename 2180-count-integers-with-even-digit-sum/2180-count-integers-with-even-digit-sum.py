class Solution:
    def countEven(self, num: int) -> int:
        def even(a):
            lst=[]
            while a>0:
                b=a%10
                lst.append(b)
                a=a//10
            return sum(lst)%2==0
        l=0
        for i in range(1,num+1):
            if even(i):
                l+=1
        return l

                
        