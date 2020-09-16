package edu.nju.ee.zerosix.yan;

import java.util.ArrayList;
import java.util.Arrays;

/*
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

        If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

        The replacement must be in-place and use only constant extra memory.

        Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

        1,2,3 - 1,3,2
        3,2,1 - 1,2,3
        1,1,5 - 1,5,1

*/
public class NextPermutation implements Solution {
    @Override
    public void run() {
        int[] input = {1,3,2};
        nextPermutation(input);
        System.out.println("NextPermutation: " + Arrays.toString(input));

    }

    public void nextPermutation(int[] nums) {
        int arrayLen = nums.length;
        for(int i = arrayLen-1; i > 0; i--){
            if(nums[i-1] < nums[i]) {
                int tmp = nums[i-1];
                int j = arrayLen - 1;
                while(j >= 0) {
                    if (nums[j] > tmp) {
                        nums[i-1] = nums[j];
                        nums[j] = tmp;
                        break;
                    }
                    j--;
                }
                int left = i;
                int right = arrayLen - 1;
                while(left < right){
                    tmp = nums[left];
                    nums[left] = nums[right];
                    nums[right] = tmp;
                    left++;
                    right--;
                }
                return;
            }
        }
        int left = 0;
        int right = arrayLen - 1;
        int tmp = 0;
        while(left < right){
            tmp = nums[left];
            nums[left] = nums[right];
            nums[right] = tmp;
            left++;
            right--;
        }
    }
}
