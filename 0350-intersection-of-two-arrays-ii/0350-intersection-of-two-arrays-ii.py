class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic={}
        lst=[]
        for i in nums1:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        for i in nums2:
            if i in dic and dic[i]!=0:
                lst.append(i)
                dic[i]-=1
        return lst
        