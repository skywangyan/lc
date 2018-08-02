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
s = Solution()
print s.maxSlidingWindow([7,2,4], 2)
