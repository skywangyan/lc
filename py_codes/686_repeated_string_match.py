# Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it.
#  If no such solution, return -1.
# For example, with A = "abcd" and B = "cdabcdab".
# Note:
# The length of A and B will be between 1 and 10000.
import math
class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        lentha, lenthb = len(A), len(B)
        times = int(math.ceil(lenthb / lentha))
        combined = A * times
        i = 0
        if B in combined:
            return times
        if B in combined+A:
            return times + 1
        if B in combined+A+A:
            return times + 2
        return -1
s = Solution()
print s.repeatedStringMatch("abcd","cdabcdab")
