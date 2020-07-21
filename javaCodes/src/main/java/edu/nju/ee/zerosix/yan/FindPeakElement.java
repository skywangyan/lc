package edu.nju.ee.zerosix.yan;

public class FindPeakElement implements Solution {
    @Override
    public void run() {
        System.out.println(findPeakElement(new int[]{1,2,3,1}));
    }

    public int findPeakElement(int[] nums) {
        if (nums.length <= 1) return 0;
        int preDelta = 0;
        for(int i = 1; i < nums.length; i++) {
            int currDelta = nums[i] - nums[i-1];
            if(preDelta > 0 && currDelta < 0){
                return i - 1;
            }
            preDelta = currDelta;
        }
        return -1;
    }
}
