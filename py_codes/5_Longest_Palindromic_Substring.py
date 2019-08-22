'''Given a string s, find the longest palindromic substring in s.
 You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
'''
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        lenth = len(s)
        def helper(m, n):
            while m >= 0 and n < lenth and s[m] == s[n]:
                m -= 1
                n += 1
            return s[m+1:n]
        
        maxl = lenth
        res = ''
        for i in xrange(lenth):
            temp = helper(i,i)
            if len(temp) > len(res):
                res = temp
            if i+1<lenth and s[i] == s[i+1]:
                temp = helper(i, i+1)
                if len(temp) > len(res):
                    res = temp
        return res

s = Solution()
print s.longestPalindrome("aba")