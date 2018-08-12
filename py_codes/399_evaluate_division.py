#!/usr/bin/python
# -*- coding: utf-8 -*-

# Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

# Example:
# Given a / b = 2.0, b / c = 3.0.
# queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
# return [6.0, 0.5, -1.0, 1.0, -1.0 ].

# The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries , where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.

# According to the example above:

# equations = [ ["a", "b"], ["b", "c"] ],
# values = [2.0, 3.0],
# queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ].
from collections import defaultdict
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        graph = defaultdict(set)
        for equation, value in zip(equations, values):
            numerator, denominator = equation[0], equation[1]
            graph[numerator].add((denominator, value))
            graph[numerator].add((numerator, 1.0))
            graph[denominator].add((numerator, 1.0 / value))
            graph[denominator].add((denominator, 1.0))
        visited = set([])
        def dfs(product, curr, target):
            if curr not in graph:
                return -1.0
            if curr == target:
                return product
            visited.add(curr)
            for nextstop,val in graph[curr]:
                if nextstop not in visited:
                    temp = dfs(product * val, nextstop, target)
                    if temp != -1:
                        visited.remove(curr)
                        return temp
            visited.remove(curr)
            return -1.0
        res = []
        for query in queries:
            start, end = query[0], query[1]
            res.append(dfs(1.0, start, end))
        return res

s = Solution()
print s.calcEquation([ ["a", "b"], ["b", "c"] ], [2.0, 3.0],[ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ])
