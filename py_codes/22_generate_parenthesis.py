class Solution(object):
    def generateParenthesis(self, n):
        res = []
        def dfs(start, curr_list):
            if start == 2 * n + 1 and sum(curr_list) == 0:
                temp = ["(" if i == 1 else ")" for i in curr_list]
                res.append("".join(temp))
                return
            if sum(curr_list) == 0 and start <= 2 * n:
                newlist = curr_list + [1]
                dfs(start+1, newlist)
            elif sum(curr_list) > 0 and start <= 2 * n:
                newlist = curr_list + [1]
                newlist1 = curr_list + [-1]
                dfs(start+1, newlist)
                dfs(start+1, newlist1)
        dfs(1,[])
        return res

t = Solution()
print t.generateParenthesis(3)
