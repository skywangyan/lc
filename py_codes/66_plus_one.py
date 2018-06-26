class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        res = []
        lenth, carry = len(digits), 0
        for i in xrange(lenth-1, -1, -1):
            if i == lenth - 1:
                curr = (digits[i] + 1) % 10
                carry = (digits[i] + 1) / 10
                res.append(curr)
            else:
                curr = (digits[i] + carry) % 10
                carry = (digits[i] + carry) / 10
                res.append(curr)
        else:
            if carry:
                res.append(1)
        res.reverse()
        return res
s = Solution()
print s.plusOne([9,9])
