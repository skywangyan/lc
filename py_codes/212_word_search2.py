#!/usr/bin/python
# -*- coding: utf-8 -*-
# Given a 2D board and a list of words from the dictionary, find all words in the board.

# Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are 
# those horizontally or vertically neighboring. The same letter cell may not be used more than once in 
# a word.

# Example:

# Input:
# words = ["oath","pea","eat","rain"] and board =
# [
#   ['o','a','a','n'],
#   ['e','t','a','e'],
#   ['i','h','k','r'],
#   ['i','f','l','v']
# ]

# Output: ["eat","oath"]
# Note:
# You may assume that all inputs are consist of lowercase letters a-z.

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        trie = {}
        for word in words:
            curr = trie
            for char in word:
                if char not in curr:
                    curr[char] = {}
                curr = curr[char]
            else:
                curr["#"] = "$"
        m,n = len(board), len(board[0])
        visited = [[0 for _ in xrange(n)] for __ in xrange(m)]
        res = set()
        def find(prev,i,j,trienode):
            if not visited[i][j]:
                visited[i][j] = 1
                if board[i][j] in trienode:
                    nextTrieNode = trienode[board[i][j]]
                    if '#' in nextTrieNode:
                        res.add(prev + board[i][j])
                    if i > 0:
                        find(prev+board[i][j], i-1, j, nextTrieNode)
                    if i < m - 1:
                        find(prev+board[i][j], i+1, j, nextTrieNode)
                    if j > 0:
                        find(prev+board[i][j], i, j-1, nextTrieNode)
                    if j < n -1:
                        find(prev+board[i][j], i, j+1, nextTrieNode)
                visited[i][j] = 0
        for i in xrange(m):
            for j in xrange(n):
                find("", i, j, trie)
        return list(res)

s = Solution()
print s.findWords([
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
], ["oath","pea","eat","rain"])
