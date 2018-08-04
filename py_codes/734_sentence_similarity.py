from collections import defaultdict
class Solution(object):
    def areSentencesSimilar(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        store = defaultdict(set)
        for pair in pairs:
            store[pair[0]] = store[pair[0]].union(set(pair))
            store[pair[1]] = store[pair[1]].union(set(pair))
        for word in words1:
            store[word].add(word)
        for word in words2:
            store[word].add(word)
        if len(words1) != len(words2):
            return False
        for i in xrange(len(words1)):
            if words2[i] not in store[words1[i]]:
                return False
        else:
            return True

s = Solution()
print s.areSentencesSimilar(["great","acting","skills"],
                            ["fine","drama","talent"],
[["great","fine"],["drama","acting"],["skills","talent"]])
