package edu.nju.ee.zerosix.yan;

public class LongestPalindromicString implements Solution {
    @Override
    public void run() {
        System.out.println(longestPalindrome("cbbd"));
    }

    public String longestPalindrome(String s) {
        class Helper {
            public int expand(String target, int left, int right) {
                int s = 0;
                int e = 0;
                while(
                        left >= 0
                        && right < target.length()
                        && target.charAt(left) == target.charAt(right)
                ){
                    s = left;
                    e = right;
                    left--;
                    right++;
                }
                return e - s + 1;
            }
        }
        Helper helper = new Helper();
        int mleft = 0;
        int mright = 0;
        int curLength = 0;
        int maxLength = 0;
        for (int i = 0; i < s.length(); i++){
            int tmp1 = helper.expand(s,i,i);
            int tmp2 = helper.expand(s,i,i+1);
            curLength = Math.max(tmp1, tmp2);
            if (curLength > maxLength) {
                mleft = i - (curLength-1) / 2;
                mright = i + curLength / 2;
                maxLength = curLength;
            }
        }

        return s.substring(mleft, mright + 1);
    }
}
