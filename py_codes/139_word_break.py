class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordlenth = len(s)
        store = [False for _ in xrange(wordlenth + 1)]
        store[0] = True
        for i in xrange(1,wordlenth+1):
            for j in xrange(i):
                if store[j] and s[j:i] in wordDict:
                    store[i] = True
        return store[-1]
s = Solution()
print s.wordBreak("catsanddog",["cats", "dog", "sand", "and", "cat"])
