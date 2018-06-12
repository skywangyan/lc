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
