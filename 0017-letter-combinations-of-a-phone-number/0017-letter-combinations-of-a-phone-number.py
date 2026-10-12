class Solution:
    d = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"]
    }

    def getLetterCombinations(self,digits,res,i=0,curr = []):
        if i == len(digits):
            seq = "".join(curr)
            res.append(seq)
            return

        for letter in self.d[digits[i]]:
            curr.append(letter)
            self.getLetterCombinations(digits,res,i+1,curr)
            curr.pop()

    def letterCombinations(self, digits: str) -> list[str]:
        res = []
        self.getLetterCombinations(digits,res)
        return res
        