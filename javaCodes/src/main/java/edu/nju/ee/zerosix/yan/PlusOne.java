package edu.nju.ee.zerosix.yan;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

/*
*
*   Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
    The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.
    You may assume the integer does not contain any leading zero, except the number 0 itself.

    Example 1:

    Input: [1,2,3]
    Output: [1,2,4]
    Explanation: The array represents the integer 123.
    Example 2:

    Input: [4,3,2,1]
    Output: [4,3,2,2]
    Explanation: The array represents the integer 4321.
* */
public class PlusOne implements Solution {
    @Override
    public void run(){
        System.out.println(Arrays.toString(plusOne(new int[]{1,2,3})));
    }

    public int[] plusOne(int[] digits) {
        ArrayList<Integer> res = new ArrayList<Integer>();
        int carry = 1;
        for(int i = digits.length - 1; i >= 0; i--){
            int curr = (digits[i] + carry) % 10;
            carry = (digits[i] + carry) / 10;
            res.add(curr);
        }
        if (carry == 1) {
            res.add(1);
        }
        int[] ret = new int[res.size()];
        for (int j = 0; j < res.size(); j++) {
            ret[j] = res.get(res.size() - 1 - j);
        }
        return ret;
    }
}
