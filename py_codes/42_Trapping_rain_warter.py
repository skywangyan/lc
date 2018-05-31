class Solution(object):
    def trap(self, height):
        left_max = [0] * len(height)
        right_max = [0] * len(height)
        left,right = 0,0
        res = 0
        for i in xrange(len(height)):
            left_max[i] = left
            left = max(left, height[i])
        for j in xrange(len(height) - 1, -1, -1):
            right_max[j] = right
            right = max(right, height[j])
        for i in xrange(len(height)):
            surface = min(left_max[i], right_max[i])
            res += surface - height[i] if surface > height[i] else 0
        return res
s = Solution()
print s.trap([0,1,0,2,1,0,1,3,2,1,2,1])
