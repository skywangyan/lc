import argparse
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m,n = len(s), len(p)
        matrix = [[0 for i in xrange(n+1)] for j in xrange(m+1)]
        for i in xrange(1,m+1):
            matrix[i][0] = 0
        matrix[0][0] = 1
        for j in xrange(1,n+1):
            if p[j-1] == "*":
                matrix[0][j] = matrix[0][j-1]
            else:
                matrix[0][j] = 0

        for i in xrange(1, m+1):
            for j in xrange(1, n+1):
                if p[j-1] == "?" or p[j-1] == s[i-1]:
                    matrix[i][j] = matrix[i-1][j-1]
                elif p[j-1] == "*":
                    x = i
                    while x >= 0:
                        if matrix[x][j-1]:
                            matrix[i][j] = 1
                            break
                        x -= 1
                    else:
                        matrix[i][j] = 0
                else:
                    matrix[i][j] = 0
        return matrix[m][n]

    def isMatch2(self, s, p):
        s_cur = 0;
        p_cur= 0;
        match = 0;
        star = -1;
        while s_cur<len(s):
            if p_cur< len(p) and (s[s_cur]==p[p_cur] or p[p_cur]=='?'):
                s_cur = s_cur + 1
                p_cur = p_cur + 1
            elif p_cur<len(p) and p[p_cur]=='*':
                match = s_cur
                star = p_cur
                p_cur = p_cur+1
            elif (star!=-1):
                p_cur = star+1
                match = match+1
                s_cur = match
            else:
                return False
        while p_cur<len(p) and p[p_cur]=='*':
            p_cur = p_cur+1
             
        if p_cur==len(p):
            return True
        else:
            return False


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("s")
    parser.add_argument("p")
    args = parser.parse_args()
    s = Solution()
    print s.isMatch2(args.s, args.p)

if __name__ == "__main__":
    main()
