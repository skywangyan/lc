class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums1, nums2 = nums1, nums2 if len(nums1) < len(nums2) else nums2, nums1
        l1 = len(nums1)
        l2 = len(nums2)
        target = (l1 + l2 + 1) / 2
        lo, hi = 0, l1 - 1
        i,j = 0,0
        while lo < hi:
            i = (lo + hi) / 2
            j = target - i
            if nums1[i-1] <= nums2[j] and nums2[j-1] <= nums[i]:
                break;
            elif i > 0 and nums1[i-1] > nums2[j]:
                hi = i - 1
            elif i < m  and nums2[j-1] > nums1[i]]:
                lo = i + 1
        if i == 0:
            maxLeft = nums2[j-1]
        elif j == 0:
            maxLeft =  nums1[i-1]
        else:
            maxLeft = max(nums1[i-1], nums2[j-1])
        if (l1 + l2) % 2 == 1:
            return maxLeft
        if i == l1:
            minRight = nums2[j]
        else:
            minRight = min(nums1[i], nums2[j])
        return (maxLeft + minRight) / 2

s = Solution()
print s.findMedianSortedArrays([1], [3,5])
