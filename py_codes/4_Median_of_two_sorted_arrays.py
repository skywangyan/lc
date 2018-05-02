class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums1, nums2 = nums1, nums2 if len(nums1) < len(nums2) else nums2, nums1
        l1 = len(nums1)
        l2 = len(nums2)
        target = (l1 + l2) / 2
        lo, hi = 0, l1 - 1
        i,j = 0,0
        while lo < hi:
            i = (lo + hi) / 2
            j = target - i
            if nums1[i] <= nums2[j+1] and nums2[j + 1] <= nums[i+1]:
                break;
            elif nums1[i] > nums2[j+1]:
                hi = mid - 1
            else:
                lo = mid + 1
        if lo <
