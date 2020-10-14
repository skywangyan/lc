package edu.nju.ee.zerosix.yan;
/*
Given a string s, you are allowed to convert it to a palindrome by adding characters in front of it.
Find and return the shortest palindrome you can find by performing this transformation.

Example 1:

Input: "aacecaaa"
Output: "aaacecaaa"
Example 2:

Input: "abcd"
Output: "dcbabcd"
 */
public class ShortestPalindrome {
    public String shortestPalindrome(String s) {
        class Impl {
            boolean isPalindrome(int target) {
                int l = 0;
                int r = target;
                while (l < r) {
                    if(s.charAt(l) == s.charAt(r)) {
                        l++;
                        r--;
                    } else {
                        return false;
                    }
                }
                return true;
            }
    }
    if(s.isEmpty()) return s;
    Impl impl = new Impl();
    for (int i = s.length() - 1; i >= 0; i--){
        if (impl.isPalindrome(i)) {
            String remaining = s.substring(i+1);
            StringBuilder x = new StringBuilder();
            x.append(remaining);
            return x.reverse().toString() + s;
        }
    }
    return s;
    }

}
