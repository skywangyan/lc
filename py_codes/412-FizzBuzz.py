class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        for i in xrange(1,n+1):
            if i % 3 == 0:
                if i % 5 == 0 :
                    res.append("FizzBuzz")
                else:
                    res.append("Fizz")
            elif i % 5 == 0:
                res.append("Buzz")
            else:
                res.append(str(i))
        return res

s = Solution()
print s.fizzBuzz(15)