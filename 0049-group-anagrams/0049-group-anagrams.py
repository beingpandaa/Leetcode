class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for ele in strs:
            count=[0]*26
            for letter in ele:
                count[ord(letter)-ord('a')]+=1
            s=str(count)
            if s in d:
                d[s].append(ele)
            else:
                d[s]=[ele]
        return d.values()
        