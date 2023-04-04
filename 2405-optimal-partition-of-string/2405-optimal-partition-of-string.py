class Solution:
    def partitionString(self, s: str) -> int:
#         d={}
#         start=0
#         count=1
#         for i in range(len(s)):
#             letter=s[i]
#             if letter in d:
#                 if d[letter]>=start:
#                     count+=1
#                     start=i
#             d[letter]=i
                    
#         return count 
        lastSeen = [-1]*26
        count = 1
        substringStarting = 0

        for i in range(len(s)):
            if lastSeen[ord(s[i]) - ord('a')] >= substringStarting:
                count += 1
                substringStarting = i
            lastSeen[ord(s[i]) - ord('a')] = i

        return count
                
                