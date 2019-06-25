'''
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''
from sets import Set
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        lenth = len(s)
        start, end = 0, 0
        cache = {}
        res = 0
        while start < lenth and end < lenth:
            if s[end] in cache and cache[s[end]] >= start:
                res = max(res, end - start)
                start = cache[s[end]] + 1
                print start
            cache[s[end]] = end
            end += 1
        res = max(res, lenth - start)
        return res

s = Solution()
print s.lengthOfLongestSubstring('abba')