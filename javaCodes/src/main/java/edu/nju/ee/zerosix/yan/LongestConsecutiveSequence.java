package edu.nju.ee.zerosix.yan;

import java.util.HashSet;
import java.util.Set;

/*
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

        Your algorithm should run in O(n) complexity.

        Example:

        Input: [100, 4, 200, 1, 3, 2]
        Output: 4
        Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
*/
public class LongestConsecutiveSequence implements Solution {
    @Override
    public void run(){
        System.out.println(longestConsecutive(new int[]{100, 4, 200, 1, 3, 2}));
    }

    public int longestConsecutive(int[] nums) {
        Set<Integer> numSet = new HashSet<>();
        for(int num : nums) {
            numSet.add(num);
        }

        int longest = 0;

        for(int num : nums) {
            if (!numSet.contains(num-1)){
                int currLongest = 0;
                while(numSet.contains(num)){
                    currLongest++;
                    numSet.remove(num);
                    num++;
                }
                longest = Math.max(longest, currLongest);

            }
        }
        return longest;
    }
}
