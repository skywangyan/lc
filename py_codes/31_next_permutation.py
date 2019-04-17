'''
Implement next permutation, which rearranges numbers into the lexicographically next
 greater permutation of numbers.
If such arrangement is not possible, it must rearrange it as the lowest possible order
 (ie, sorted in ascending order).
The replacement must be in-place and use only constant extra memory.
Here are some examples. Inputs are in the left-hand column and its corresponding 
outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
'''

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        lenth = len(nums)
        i = lenth - 1
        while i > 0:
            if nums[i-1] < nums[i]:
                j = lenth -1
                while j > i  and nums[j] <= nums[i-1]:
                    j -= 1
                nums[i-1], nums[j] = nums[j], nums[i-1]
                temp = nums[i:]
                temp.reverse()
                nums[i:] = temp
                return
            else:
                i -= 1
        nums.reverse()
                
s = Solution()
a = [1,2]
s.nextPermutation(a)
print a
