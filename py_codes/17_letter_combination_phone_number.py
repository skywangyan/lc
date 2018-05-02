class Solution(object):
    def letterCombination(self, digits):
        letterMap = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        res, maxLength = [], len(digits)
        def dfs(already, start):
            if start == maxLength:
                res.append(already)
                return
            for char in letterMap.get(digits[start]):
                dfs(already+char, start+1)
        dfs("", 0)
        return res

sl = Solution()
print sl.letterCombination("23")
