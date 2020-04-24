package edu.nju.ee.zerosix.yan;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
 *
 * You may assume that the intervals were initially sorted according to their start times.
 *
 * Example 1:
 *
 * Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
 * Output: [[1,5],[6,9]]
 * Example 2:
 *
 * Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
 * Output: [[1,2],[3,10],[12,16]]
 * Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
 */

public class InsertInterval implements Solution {
    @Override
    public void run(){
        for(int[] x : insert(
                new int[][]{
                        new int[]{1,5}
                }, new int[]{2,7}
        )
        ) {
            System.out.println(Arrays.toString(x));
        }
    }

    public int[][] insert(int[][] intervals, int[] newInterval) {
        int l = intervals.length;
        List<int[]> buffer = new ArrayList<int[]>();
        List<int[]> res = new ArrayList<int[]>();
        if (l == 0) return new int[][]{ newInterval };
        boolean inserted = false;
        for(int[] intv : intervals) {
            if (intv[0] < newInterval[0]) {
                buffer.add(intv);
            } else if (!inserted) {
                buffer.add(newInterval);
                buffer.add(intv);
                inserted = true;
            } else {
                buffer.add(intv);
            }
        }
        if (!inserted) {
            buffer.add(newInterval);
        }
        int[] curr = buffer.get(0);
        for (int[] inv: buffer) {
            if (inv[0] <= curr[1]) {
                curr[1] = Math.max(curr[1], inv[1]);
            } else {
                res.add(curr);
                curr = inv;
            }
        }
        res.add(curr);
        return res.toArray(new int[res.size()][]);
    }
}
