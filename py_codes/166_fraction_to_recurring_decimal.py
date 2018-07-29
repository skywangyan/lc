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
