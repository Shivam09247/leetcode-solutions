class Solution:
    def rearrangeArray(self, nums):
        dic = {}
        for x in nums:
            if x in dic:
                dic[x] += 1
            else:
                dic[x] = 1

        ans = []

        while dic:
            for x in sorted(dic):
                ans.append(x)

            for x in list(dic):
                dic[x] -= 1

                if dic[x] == 0:
                    del dic[x]

        return ans