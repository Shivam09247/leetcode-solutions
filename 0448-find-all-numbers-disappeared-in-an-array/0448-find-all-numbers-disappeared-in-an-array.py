class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s=set()
        for i in nums:
            s.add(i)
        lst=[]
        for i in range(1,len(nums)+1):
            if i not in s:
                lst.append(i)
        return lst

        