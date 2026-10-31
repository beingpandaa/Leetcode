class Solution:
    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        diff = [0 for i in range(len(s)+1)]
        for start, end, direction in shifts:
            change = 1 if direction == 1 else -1
            diff[start]+=change
            diff[end+1]-=change

        s=list(s)
        running = 0
        for i in range(len(s)):
            running += diff[i]
            total = ord(s[i]) + running
            s[i] = chr(ord('a')+(total-ord('a'))%26)
        return ''.join(s)
        