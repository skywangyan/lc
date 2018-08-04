from collections import defaultdict
class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        store = defaultdict(int)
        for char in s:
            store[char] += 1
        oddNum = 0
        for k in store:
            if store[k] % 2 == 1:
                oddNum += 1
        return True if oddNum <= 1 else False
s = Solution()
print s.canPermutePalindrome("aab")
