class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        s = set(nums)
        d={}
        lcs = 0
        for ele in s:
            curr = 1
            lookupElement = ele-1
            while lookupElement in s:
                if lookupElement in d:
                    curr+=d[lookupElement]
                    break
                lookupElement-=1
                curr+=1
            d[ele]=curr
            lcs = max(lcs,curr)
        return lcs

