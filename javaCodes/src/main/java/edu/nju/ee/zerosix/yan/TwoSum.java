package edu.nju.ee.zerosix.yan;

import java.util.HashMap;
import java.util.Map;

public class TwoSum implements Solution {
    public void run() {
        int[] result = (twoSum(new int[]{2,7,11,15}, 9));
        for (int i : result) {
            System.out.println(i);
        }
    }

    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for(int i = 0; i < nums.length; i++) {
            map.put(nums[i], i);
        }
        for(int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (map.containsKey(complement) && map.get(complement) != i) {
                return new int[] {i, map.get(complement)};
            }
        }
        throw new IllegalArgumentException("No two sum solution!");
    }
}
