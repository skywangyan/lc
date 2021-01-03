package edu.nju.ee.zerosix.yan;

import java.util.Stack;
/*
Given a string s representing an expression, implement a basic calculator to evaluate it.

Example 1:

Input: s = "1 + 1"
Output: 2

Example 2:

Input: s = " 2-1 + 2 "
Output: 3

Example 3:

Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23


Constraints:

1 <= s.length <= 3 * 105
s consists of digits, '+', '-', '(', ')', and ' '.
s represents a valid expression.
 */
public class BasicCalculator {
    public int calculate(String s) {
        Stack<Integer> numbers = new Stack<>();
        Integer operand = 0;
        Integer result = 0;
        Integer sign = 1;

        for(int i = 0; i < s.length(); i++){
            Character c = s.charAt(i);
            if (Character.isDigit(c)) {
                operand = operand * 10 + Integer.parseInt(c.toString());
            } else if (c == '+') {
                result += operand * sign;
                operand = 0;
                sign = 1;
            } else if (c == '-') {
                result += operand * sign;
                operand = 0;
                sign = -1;
            } else if (c == '(') {
                numbers.push(result);
                //push sign for the whole ()
                numbers.push(sign);
                result = 0;
                operand = 0;
                sign = 1;
            } else if (c == ')') {
                result += sign * operand;
                result *= numbers.pop();
                result += numbers.pop();
                operand = 0;
                sign = 1;
            }
        }
        return result + sign * operand;
    }
}
