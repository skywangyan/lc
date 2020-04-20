package edu.nju.ee.zerosix.yan;

/*
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

        '?' Matches any single character.
        '*' Matches any sequence of characters (including the empty sequence).
        The matching should cover the entire input string (not partial).

        Note:

        s could be empty and contains only lowercase letters a-z.
        p could be empty and contains only lowercase letters a-z, and characters like ? or *.
        Example 1:

        Input:
        s = "aa"
        p = "a"
        Output: false
        Explanation: "a" does not match the entire string "aa".
        Example 2:

        Input:
        s = "aa"
        p = "*"
        Output: true
        Explanation: '*' matches any sequence.
        Example 3:

        Input:
        s = "cb"
        p = "?a"
        Output: false
        Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
        Example 4:

        Input:
        s = "adceb"
        p = "*a*b"
        Output: true
        Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
        Example 5:

        Input:
        s = "acdcb"
        p = "a*c?b"
        Output: false
*/

public class WildcardMatching implements Solution {
    @Override
    public void run(){
        System.out.println("WildcardMatching: " + isMatch("acdcb","a*c?b"));
    }

    public boolean isMatch(String s, String p) {
        int sLen = s.length();
        int pLen = p.length();
        boolean[][] matrix = new boolean[sLen + 1][pLen + 1];
        matrix[0][0] = true;
        for(int i = 1; i < sLen + 1; i++) {
            matrix[i][0] = false;
        }
        for (int j = 1; j < pLen + 1; j++) {
            if(p.charAt(j - 1) != '*') {
                matrix[0][j] = false;
            } else {
                matrix[0][j] = matrix[0][j-1];
            }
        }

        for(int i = 1; i < sLen + 1; i++){
            for(int j = 1; j < pLen + 1; j++) {
                if (p.charAt(j-1) == '?' || p.charAt(j-1) == s.charAt(i-1)) {
                    matrix[i][j] = matrix[i-1][j-1];
                } else if (p.charAt(j-1) == '*') {
                    matrix[i][j] = matrix[i][j-1] || matrix[i-1][j];
                }
            }
        }
        return matrix[sLen][pLen];
    }
}
