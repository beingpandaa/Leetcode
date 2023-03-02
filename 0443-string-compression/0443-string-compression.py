class Solution:
    def compress(self, chars: List[str]) -> int:
        index=0
        j=0
        i=0
        while i<len(chars):
            while i<len(chars) and chars[i]==chars[j]:
                i+=1
            chars[index]=chars[j]
            index+=1
            if i-j>1:
                for ele in str(i-j):
                    chars[index]=ele
                    index+=1
            j=i

        return index
    
                