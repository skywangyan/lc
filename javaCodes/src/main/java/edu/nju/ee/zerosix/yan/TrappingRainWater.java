package edu.nju.ee.zerosix.yan;
/*
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it is able to trap after raining.
The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
In this case, 6 units of rain water (blue section) are being trapped.

        Example:

        Input: [0,1,0,2,1,0,1,3,2,1,2,1]
        Output: 6
*/
public class TrappingRainWater implements Solution{
    @Override
    public void run(){
        System.out.println("TrappingRainWater:" + trap(new int[]{0,1,0,2,1,0,1,3,2,1,2,1}));
    }

    public int trap(int[] height) {
        int[] leftHighest = new int[height.length];
        int[] rightHighest = new int[height.length];
        int highest = 0;
        for (int i = 0; i< height.length; i++){
            leftHighest[i] = highest;
            highest = Math.max(highest, height[i]);
        }
        highest = 0;
        for (int j = height.length - 1; j >=0; j--) {
            rightHighest[j] = highest;
            highest = Math.max(highest, height[j]);
        }
        int res = 0;
        for(int i = 0; i < height.length; i++) {
            res += Math.max(Math.min(leftHighest[i], rightHighest[i]) - height[i], 0);
        }
        return res;
    }
}
