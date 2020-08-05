package edu.nju.ee.zerosix.yan;

/*
Given two integers representing the numerator and denominator of a fraction,
return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

If multiple answers are possible, just return any of them.

Example 1:

Input: numerator = 1, denominator = 2
Output: "0.5"
Example 2:

Input: numerator = 2, denominator = 1
Output: "2"
Example 3:

Input: numerator = 2, denominator = 3
Output: "0.(6)"
 */

import java.util.HashMap;
import java.util.Map;

public class FractionToRecurringDecimal implements Solution {
    @Override
    public void run() {
        System.out.println(fractionToDecimal(-1,-2147483648));
    }

    public String fractionToDecimal(int numerator, int denominator) {
        if (numerator == 0) {
            return "0";
        }
        StringBuilder container = new StringBuilder();
        //check flag
        if ((numerator < 0) != (denominator < 0)) {
            container.append("-");
        }
        long numeratorAbs = Math.abs((long)numerator);
        long denominatorAbs = Math.abs((long)denominator);
        long intPart = numeratorAbs / denominatorAbs;
        container.append(intPart);
        long remainder = numeratorAbs % denominatorAbs;
        if(remainder == 0) {
            return container.toString();
        }
        else {
            container.append(".");
        }

        Map<Long, Integer> store = new HashMap<>();
        long curr;
        while (remainder != 0){
            if (!store.containsKey(remainder)) {
                store.put(remainder, container.length());
                curr = remainder * 10 / denominatorAbs;
                container.append(curr);
                remainder = (remainder * 10) % denominator;
            } else {
                int index = store.get(remainder);
                container.insert(index, '(');
                container.append(')');
                break;
            }
        }
        return container.toString();
    }
}
