class Solution:
    def countSeniors(self, details: List[str]) -> int:
        l = 0
        for i in details:
            a = i[11:13]
            if int(a) > 60:
                l += 1
        return l
        