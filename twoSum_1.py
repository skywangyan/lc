from utils import logger
class Solution(object):
    @logger
    def twoSum(self, nums, target):
        store = {}
        for i in xrange(len(nums)):
            if nums[i] not in store:
                store[nums[i]] = [i]
            else:
                store[nums[i]].append(i)
        print store
        for j in nums:
            if target - j in store:
                if target - j != j:
                    return [store[j][0], store[target-j][0]]
                elif len(store[j]) == 2:
                    return store[j]
        return []

if __name__ == "__main__":
    instance = Solution()
    print instance.twoSum([3,2,4],6)
