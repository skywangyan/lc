'''Given a non-empty array of digits representing a non-negative integer, 
plus one to the integer.
The digits are stored such that the most significant digit is at the head of the list, 
and each element in the array contain a single digit.
You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:
Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

Example 2:
Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
'''
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
