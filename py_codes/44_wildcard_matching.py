'''
Given an input string (s) and a pattern (p), implement wildcard pattern matching with 
support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like ? or *.

Example 1:
Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input:
s = "aa"
p = "*"
Output: true
Explanation: '*' matches any sequence.

Example 3:
Input:
s = "cb"
p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.

Example 4:
Input:
s = "adceb"
p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the 
substring "dce".

Example 5:
Input:
s = "acdcb"
p = "a*c?b"
Output: false
'''
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
        return True if matrix[m][n] else False

    


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("s")
    parser.add_argument("p")
    args = parser.parse_args()
    s = Solution()
    print s.isMatch(args.s, args.p)

if __name__ == "__main__":
    main()
