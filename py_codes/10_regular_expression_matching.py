class Solution(object):
    def isMatch(self, s, p):
        l1 = len(s) + 1
        l2 = len(p) + 1
        matrix = [[0 for i in xrange(l1)] for _ in xrange(l2)]
        matrix[0][0] = 1
        for j in xrange(1, l2):
            if p[j-1] == '*':
                matrix[j][0] = matrix[j-2][0] if j >= 2 else matrix[j-1][0]
            else:
                matrix[j][0] = 0
        for i in xrange(1, l2):
            for j in xrange(1, l1):
                if p[i-1] == s[j-1]:
                    matrix[i][j] = matrix[i-1][j-1]
                elif p[i-1] == '.':
                    matrix[i][j] = matrix[i-1][j-1]
                elif p[i-1] == "*":
                    if i == 1:
                        matrix[i][j] == matrix[0][j]
                    elif i >= 2 and (p[i-2] == s[j-1] or p[i-2] == '.'):
                        matrix[i][j] = matrix[i][j-1] or matrix[i-1][j] or matrix[i-2][j]
                    else:
                        matrix[i][j] =matrix[i-2][j]
                else:
                    matrix[i][j] = 0
        return True if matrix[l2-1][l1-1] else False

test = Solution()

print test.isMatch("aab", "c*a*b")
