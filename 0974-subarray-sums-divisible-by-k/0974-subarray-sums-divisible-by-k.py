class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        pfsum=0
        rem_dic={0:1}
        count=0
        for i in nums:
            pfsum+=i
            rem=pfsum%k
            if rem in rem_dic:
                count+=rem_dic[rem]
            rem_dic[rem]=rem_dic.get(rem,0)+1
        return count

        