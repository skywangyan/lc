# Given two sentences words1, words2 (each represented as an array of strings), and a list of similar word pairs pairs, determine if two sentences are similar.

# For example, words1 = ["great", "acting", "skills"] and words2 = ["fine", "drama", "talent"] are similar, if the similar word pairs are pairs = [["great", "good"], ["fine", "good"], ["acting","drama"], ["skills","talent"]].

# Note that the similarity relation is transitive. For example, if "great" and "good" are similar, and "fine" and "good" are similar, then "great" and "fine" are similar.

# Similarity is also symmetric. For example, "great" and "fine" being similar is the same as "fine" and "great" being similar.

# Also, a word is always similar with itself. For example, the sentences words1 = ["great"], words2 = ["great"], pairs = [] are similar, even though there are no specified similar word pairs.

# Finally, sentences can only be similar if they have the same number of words. So a sentence like words1 = ["great"] can never be similar to words2 = ["doubleplus","good"].

# Note:

# The length of words1 and words2 will not exceed 1000.
# The length of pairs will not exceed 2000.
# The length of each pairs[i] will be 2.
# The length of each words[i] and pairs[i][j] will be in the range [1, 20].
from collections import defaultdict
class UnionFind(object):
    def __init__(self, n):
        self.root = range(n)
    def find(self, inx):
        if inx != self.root[inx]:
            self.root[inx] = self.find(self.root[inx])
        return self.root[inx]
    def union(self, index1, index2):
        self.root[self.find(index1)] = self.find(index2)

class Solution(object):
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2):
            return False
        uf = UnionFind(2 * len(pairs))
        index = 0
        store = {}
        for pair in pairs:
            if pair[0] not in store:
                store[pair[0]] = index
                index += 1
            if pair[1] not in store:
                store[pair[1]] = index
                index += 1
            uf.union(store[pair[0]], store[pair[1]])
        print uf.root
        print store
        for i in xrange(len(words1)):
            if words1[i] == words2[i]:
                continue
            if words1[i] not in store or words2[i] not in store:
                print "words not in store: ", i
                return False
            if uf.find(store[words1[i]]) != uf.find(store[words2[i]]):
                print "find does not match: ", i, words1[i], words2[i]
                return False
        return True

s = Solution()
print s.areSentencesSimilarTwo(["this","summer","thomas","get","really","very","rich","and","have","any","actually","wonderful","and","good","truck","every","morning","he","drives","an","extraordinary","truck","around","the","nice","city","to","eat","some","extremely","extraordinary","food","as","his","meal","but","he","only","entertain","an","few","well","fruits","as","single","lunch","he","wants","to","eat","single","single","and","really","healthy","life"],
                               ["this","summer","thomas","get","very","extremely","rich","and","possess","the","actually","great","and","wonderful","vehicle","every","morning","he","drives","unique","extraordinary","automobile","around","unique","fine","city","to","drink","single","extremely","nice","meal","as","his","super","but","he","only","entertain","a","few","extraordinary","food","as","some","brunch","he","wants","to","take","any","some","and","really","healthy","life"],
[["good","nice"],["good","excellent"],["good","well"],["good","great"],["fine","nice"],["fine","excellent"],["fine","well"],["fine","great"],["wonderful","nice"],["wonderful","excellent"],["wonderful","well"],["wonderful","great"],["extraordinary","nice"],["extraordinary","excellent"],["extraordinary","well"],["extraordinary","great"],["one","a"],["one","an"],["one","unique"],["one","any"],["single","a"],["single","an"],["single","unique"],["single","any"],["the","a"],["the","an"],["the","unique"],["the","any"],["some","a"],["some","an"],["some","unique"],["some","any"],["car","vehicle"],["car","automobile"],["car","truck"],["auto","vehicle"],["auto","automobile"],["auto","truck"],["wagon","vehicle"],["wagon","automobile"],["wagon","truck"],["have","take"],["have","drink"],["eat","take"],["eat","drink"],["entertain","take"],["entertain","drink"],["meal","lunch"],["meal","dinner"],["meal","breakfast"],["meal","fruits"],["super","lunch"],["super","dinner"],["super","breakfast"],["super","fruits"],["food","lunch"],["food","dinner"],["food","breakfast"],["food","fruits"],["brunch","lunch"],["brunch","dinner"],["brunch","breakfast"],["brunch","fruits"],["own","have"],["own","possess"],["keep","have"],["keep","possess"],["very","super"],["very","actually"],["really","super"],["really","actually"],["extremely","super"],["extremely","actually"]])
