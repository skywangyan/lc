'''
Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
'''

import argparse
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n == 0:
            return 1.0
        curr, res  = 1, x
        while curr * 2 <= n:
            curr = curr * 2
            res = res * res
        else:
            return res * self.myPow(x, n - curr)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("x")
    parser.add_argument("n")
    args = parser.parse_args()
    s = Solution()
    print s.myPow(int(args.x), int(args.n))

        
if __name__ == "__main__":
    main()
