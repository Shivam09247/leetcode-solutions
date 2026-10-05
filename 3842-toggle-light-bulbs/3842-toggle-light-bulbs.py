class Solution:
    def toggleLightBulbs(self, bulbs):
        dic = {}

        for x in bulbs:
            if x in dic:
                del dic[x]
            else:
                dic[x] = 1

        return sorted(dic)