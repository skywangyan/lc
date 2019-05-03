'''
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

Example 1:

Input: numerator = 1, denominator = 2
Output: "0.5"
Example 2:

Input: numerator = 2, denominator = 1
Output: "2"
Example 3:

Input: numerator = 2, denominator = 3
Output: "0.(6)"

'''

class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        res = []
        store = {}
        idx1 = None
        flag = -1 if numerator * denominator < 0 else 1
        numerator, denominator = abs(numerator), abs(denominator)
        while 1:
            temp = numerator / denominator
            rest = numerator % denominator
            res.append(str(temp))
            if rest == 0:
                break
            if rest not in store:
                store[rest] = len(res) - 1
            else:
                idx1 = store[rest]
                break
            numerator = rest * 10
        flagstr = "" if flag == 1 else "-"
        print res
        if len(res) == 1:
            return flagstr + res[0]
        if idx1 == None:
            return flagstr + res[0] + "." + "".join(res[1:])
        else:
            return flagstr + res[0] + "." + "".join(res[1:idx1+1]) + "(" + "".join(res[idx1+1:]) + ")"

s = Solution()
print s.fractionToDecimal(-50,8)
