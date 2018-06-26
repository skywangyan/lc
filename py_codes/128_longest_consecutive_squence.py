from sets import Set
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype
        """
        allNums = Set(nums)
        longest = 0
        for num in nums:
            if num in allNums:
                tmp_longest = 1
                allNums.remove(num)
                prev = num - 1
                nextnum = num + 1
                while prev in allNums:
                    tmp_longest += 1
                    allNums.remove(prev)
                    prev -= 1
                while nextnum in allNums:
                    tmp_longest += 1
                    allNums.remove(nextnum)
                    nextnum += 1
                longest = max(longest, tmp_longest)
        return longest

s = Solution()
print s.longestConsecutive([100, 4, 200, 1, 3, 2])
                
            
