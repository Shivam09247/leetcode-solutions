class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic={}
        for i in arr:
            dic[i]=dic.get(i,0)+1
        lst=[i for i in dic.values()]
        s=set(lst)
        if len(lst)==len(s):
            return True
        return False
