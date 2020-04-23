package edu.nju.ee.zerosix.yan;
/*
* Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
*
*/
import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Stack;
public class MergeIntervals implements Solution {
    @Override
    public void run(){
        for(int[] x : merge(new int[][]{
                new int[]{1,3},
                new int[]{2,6},
                new int[]{8,10},
                new int[]{15,18}
        })){
            System.out.println(Arrays.toString(x));
        }

    }

    public int[][] merge(int[][] intervals) {
        if(intervals.length <= 1) return intervals;
        Stack<int[]> st = new Stack<int[]>();
        Arrays.sort(intervals, (i1, i2) -> Integer.compare(i1[0], i2[0]));
        List<int[]> res = new ArrayList<int[]>();
        int[] currIntv = intervals[0];
        for (int[] intv: intervals) {
            if(currIntv[1] >= intv[0]) {
                currIntv = new int[]{currIntv[0], Math.max(currIntv[1], intv[1])};
            } else {
                res.add(currIntv);
                currIntv = intv;
            }
        }
        res.add(currIntv);
        return res.toArray(new int[res.size()][]);
    }
}
