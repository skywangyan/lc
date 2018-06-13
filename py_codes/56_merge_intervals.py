# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        orderedIntervals = sorted(intervals, key=lambda x: x.start)
        res = []
        for ivl in orderedIntervals:
            if not res:
                res.append(ivl)
            else:
                if res[-1].end < ivl.start:
                    res.append(ivl)
                else:
                    last = res.pop()
                    newivl = Interval(last.start, max(last.end, ivl.end))
                    res.append(newivl)
        return res
s = Solution()
for i in s.merge([Interval(1,4), Interval(4,5)]):
    print i.start, i.end
                
