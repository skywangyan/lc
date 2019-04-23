'''
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
You may assume that the intervals were initially sorted according to their start times.

Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

'''

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        res = []
        merged = False
        for inv in intervals:
            if inv.end < newInterval.start and not merged:
                res.append(inv)
            elif inv.end >= newInterval.start and inv.start <= newInterval.end and not merged:
                temp = Interval(min(inv.start, newInterval.start), max(inv.end, newInterval.end))
                res.append(temp)
                merged = True
            elif inv.start > newInterval.end and not merged:
                res.append(newInterval)
                res.append(inv)
                merged = True
            elif merged:
                last = res.pop()
                if not last.end < inv.start:
                    temp = Interval(last.start, max(last.end, inv.end))
                    res.append(temp)
                else:
                    res.append(last)
                    res.append(inv)
        if not merged:
            res.append(newInterval)
        return res

    def insert2(self, intervals, newInterval):
        res = []
        merged = False
        for inv in intervals:
            if not merged:
                if inv[0] > newInterval[1] or inv[1] < newInterval[0]:
                    if inv[0] < newInterval[0]:
                        res.append(inv)
                    else:
                        res.append(newInterval)
                        res.append(inv)
                        merged = True
                else:
                    res.append([min(inv[0], newInterval[0]), max(inv[1], newInterval[1])])
                    merged = True
            else:
                if not (res[-1][0] > inv[1] or res[-1][1] < inv[0]):
                    last = res.pop()
                    res.append([min(last[0], inv[0]), max(last[1], inv[1])])
                else:
                    res.append(inv)
        if not res or not merged:
            res.append(newInterval)
        return res
s = Solution()
print s.insert2([[1,5]], [6,8])
                
