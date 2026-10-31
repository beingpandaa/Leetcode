class Solution:
    def shiftingLetters(self, s: str, shifts: list[int]) -> str:
        for i in range(len(shifts)-2,-1,-1):
            shifts[i]+=shifts[i+1]
        s=list(s)
        for i in range(len(s)):
            position = ord(s[i]) - ord('a')
            shifted = (position + shifts[i]) % 26
            s[i] = chr(ord('a') + shifted)
        return ''.join(s)
