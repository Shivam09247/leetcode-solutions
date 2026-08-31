class Solution:
    def toLowerCase(self, s: str) -> str:
        S=""
        for i in s:
            a=ord(i)
            if 65 <= a <= 90:
                S+=chr(a+32)
            else:
                S+=i
        return S

        