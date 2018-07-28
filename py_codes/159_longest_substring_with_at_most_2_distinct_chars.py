class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        currTwoChars = {}
        start = 0
        res = 0
        i = 0
        while i < length:
            if s[i] in currTwoChars:
                currTwoChars[s[i]] = i
                res = max(i - start + 1, res)
                i += 1
            else:
                if len(currTwoChars) < 2:
                    currTwoChars[s[i]] = i
                    res = max(i - start + 1, res)
                    i += 1
                else:
                    small, big = None, None
                    for char in currTwoChars:
                        if not big:
                            big = char
                        else:
                            if currTwoChars[char] < currTwoChars[big]:
                                small = char
                            else:
                                small = big
                                big = char
                    start = currTwoChars[small] + 1
                    currTwoChars.pop(small)
                    currTwoChars[s[i]] = i
                    res = max(i-start+1, res)
                    i += 1


        return res

s = Solution()
print s.lengthOfLongestSubstringTwoDistinct("a")
