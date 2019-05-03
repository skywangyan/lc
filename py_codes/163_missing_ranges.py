'''
"""
Given a sorted integer array where the range of elements are [lower, upper] inclusive, return its missing ranges.
For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99, return ["2", "4->49", "51->74", "76->99"].
"""
'''
class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        res = []
        gapl = lower
        for num in nums:
            if gapl == num:
                gapl += 1
            elif gapl < num:
                gapr = num - 1
                if gapl == gapr:
                    res.append(str(gapl))
                else:
                    res.append(str(gapl) + "->" + str(gapr))
                gapl = num + 1
        if gapl < upper:
            res.append(str(gapl) + "->" + str(upper))
        elif gapl == upper:
            res.append(str(gapl))
        return res

    def findMissingRanges2(self, nums, lower, upper):
        left = lower
        res = []
        for num in nums:
            if left < num:
                right = num - 1
                res.append("{0}->{1}".format(left,right) if left < right else "{0}".format(left))
                left = num + 1
            elif left == num:
                left += 1
        else:
            if left <= upper:
                res.append("{0}->{1}".format(left,upper) if left < upper else "{0}".format(left))
        return res
s = Solution()
print s.findMissingRanges2([0, 1, 3, 50, 75],0,75)
