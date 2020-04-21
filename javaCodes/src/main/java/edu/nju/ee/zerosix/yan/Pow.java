package edu.nju.ee.zerosix.yan;

/*
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
*/

public class Pow implements Solution{
    @Override
    public void run(){
        System.out.println(myPow(1.0, -2147483648));
    }

    public double myPow(double x, int n) {
        if(n == 0) return 1.0;
        if(x == 1.0) return 1.0;
        if(x == -1){
            return  n % 2 == 0 ? 1:-1;
        }
        if(n == Integer.MIN_VALUE) return 0;
        if(n < 0) return 1 / myPow(x, -n);
        int currIndex = 1;
        double res = x;
        Double upperLimit = Math.pow(2,30);
        while (currIndex < upperLimit && currIndex * 2 <= n) {
            currIndex = currIndex * 2;
            res = res * res;
        }
        if (currIndex < n) {
            return  res * myPow(x, n - currIndex);
        } else {
            return res;
        }
    }
}
