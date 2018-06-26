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

s = Solution()
for i in s.insert([Interval(1,3), Interval(6, 9)], Interval(2,5)):
    print i.start, i.end

                
