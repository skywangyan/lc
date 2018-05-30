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
a = [1,5,1]
s.nextPermutation(a)
print a
