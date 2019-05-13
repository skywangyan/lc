'''
Given an array nums, there is a sliding window of size k which is moving from the very left of the
 array to the very right. You can only see the k numbers in the window. Each time the sliding window 
 moves right by one position. Return the max sliding window.

Example:

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7] 
Explanation: 

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Note: 
You may assume k is always valid, 1 ≤ k ≤ input array's size for non-empty array.

Follow up:
Could you solve it in linear time?
'''
from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []
        res = [None] * (len(nums) - k + 1)
        q = deque()
        idx = 0
        for i in xrange(len(nums)):
            print q
            while len(q) > 0 and q[0] < i - k + 1:
                q.popleft()
            while len(q) > 0 and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
            print q
            if i >= k - 1:
                res[idx] = nums[q[0]]
                idx += 1
        return res
    
    def maxSlidingWindow2(self, nums, k):
        window = deque()
        res = []
        for i in xrange(len(nums)):
            while window and  window[0] < i - k + 1:
                window.popleft()
            while window and nums[window[-1]] < nums[i]:
                window.pop()
            window.append(i)
            if window and i >= k - 1:
                res.append(nums[window[0]])
        return res
s = Solution()
print s.maxSlidingWindow2([7,2,4], 2)
