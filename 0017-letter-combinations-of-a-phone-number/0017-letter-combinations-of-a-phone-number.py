class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits=="":
            return []
        d={2:['a','b','c'],3:['d','e','f'],4:['g','h','i'],5:['j','k','l'],6:['m','n','o'],
   7:['p','q','r','s'],8:['t','u','v'],9:['w','x','y','z']}
        def dfs(i=0):
            if i==len(digits)-1:
                return d[int(digits[len(digits)-1])]
            op=[]
            small_op=dfs(i+1)
            for letter in d[int(digits[i])]:
                for comb in small_op:
                    op.append(letter+comb)
            return op
        return dfs()