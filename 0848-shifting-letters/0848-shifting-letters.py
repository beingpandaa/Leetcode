class Solution:
    def shiftingLetters(self, s: str, shifts: list[int]) -> str:
        for i in range(len(shifts)-2,-1,-1):
            shifts[i]+=shifts[i+1]
        s=list(s)
        for i in range(len(s)):
            total = ord(s[i]) + shifts[i]
            
            s[i] = chr(ord('a')+(total-ord('a'))%26)
        return ''.join(s)
