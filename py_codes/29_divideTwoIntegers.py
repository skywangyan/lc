'''
Given two integers dividend and divisor, divide two integers without using 
multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Note:

Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
Assume we are dealing with an environment which could only store integers
 within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of
  this problem, assume that your function returns 231 − 1 when the division 
  result overflows.
'''

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        isPositive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        def log(div, dvs):
            if div < dvs:
                return 0, 0
            tmp = 1
            while div >= dvs:
                tmp = tmp << 1
                dvs = dvs << 1

            tmp >>= 1
            return tmp, div - (dvs >> 1)
        res = 0
        while dividend >= divisor:
            curr, remaining = log(dividend, divisor)
            res += curr
            dividend = remaining
        return res if isPositive else 0 - res
s = Solution()
print s.divide(7, -3)