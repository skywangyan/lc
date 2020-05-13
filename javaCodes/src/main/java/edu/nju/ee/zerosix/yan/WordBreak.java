package edu.nju.ee.zerosix.yan;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
/*
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words,
 determine if s can be segmented into a space-separated sequence of one or more dictionary
 words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
 */
public class WordBreak implements Solution {
    @Override
    public void run() {
        System.out.println(wordBreak("leetcode", new ArrayList<String>(Arrays.asList("leet", "code"))));
    }

    public boolean wordBreak(String s, List<String> wordDict) {
        ArrayList<Boolean> dp = new ArrayList<>(Collections.nCopies(s.length()+1, false));
        dp.set(0, true);
        for(int i = 1; i < dp.size(); i++) {
            int j = 0;
            for(; j < i; j++){
                if (dp.get(j) && wordDict.contains(s.substring(j,i))) {
                    dp.set(i, true);
                    break;
                }
            }
            if (j == i) {
                dp.set(i, false);
            }

        }
        System.out.println(dp);
        return dp.get(s.length());
    }
}
