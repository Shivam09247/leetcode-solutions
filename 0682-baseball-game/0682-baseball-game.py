class Solution:
    def calPoints(self, operations: List[str]) -> int:
        lst=[]
        for i in operations:
            if i=="+":
                if len(lst)>=2:
                    a=lst[-2]
                    b=lst[-1]
                elif len(lst)>0:
                    a=0
                    b=lst[-1]
                lst.append(int(a)+int(b))
            elif i=="D":
                if lst:
                    a=lst[-1]
                lst.append(int(a)*2)
            elif i=="C":
                lst.pop()
            else:
                lst.append(i)
        return sum([int(i) for i in lst])
        