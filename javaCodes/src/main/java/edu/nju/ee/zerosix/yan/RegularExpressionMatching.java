package edu.nju.ee.zerosix.yan;
/*
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:

Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
 */
public class RegularExpressionMatching implements Solution {
    @Override
    public void run() {
        System.out.println(isMatch("aab", "c*a*b"));
    }
    public boolean isMatch(String s, String p) {
        int slenth = s.length();
        int plenth = p.length();
        Boolean[][] dp = new Boolean[plenth+1][slenth+1];
        dp[0][0] = true;
        for (int i = 1; i <= slenth; i++) {
            dp[0][i] = false;
        }
        for (int j = 1; j <= plenth; j++) {
            if (p.charAt(j-1) == '*') {
                dp[j][0] = dp[j-2][0];
            } else {
                dp[j][0] = false;
            }
        }
        for (int i = 1; i <= plenth; i++) {
            for (int j = 1; j <= slenth; j++) {
                if (p.charAt(i-1) == '.') {
                    dp[i][j] = dp[i-1][j-1];
                } else if (p.charAt(i-1) == '*') {
                    if (p.charAt(i-2) == '.' || p.charAt(i-2) == s.charAt(j-1)) {
                        dp[i][j] = dp[i][j-1] || // * for 1+ match
                                dp[i-2][j] || // 0 match
                                dp[i-1][j-1]; // 1 match
                    }else if (p.charAt(i-2) != s.charAt(j-1)) {
                        dp[i][j] = dp[i-2][j];
                    }
                } else {
                    dp[i][j] = dp[i-1][j-1] && p.charAt(i-1) == s.charAt(j-1);
                }

            }
        }
        return dp[plenth][slenth];
    }
}
