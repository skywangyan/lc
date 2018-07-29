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


s = Solution()
print s.findMissingRanges([1,1,1],1,1)
