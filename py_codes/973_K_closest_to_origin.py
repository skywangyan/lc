from heapq import heappush, heappop

class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        def dist(point):
            return point[0] * point[0] + point[1] * point[1]
        min_heap = []
        res = []
        for point in points:
            heappush(min_heap, (dist(point), point))
        for i in xrange(K):
            res.append(heappop(min_heap)[1])
        return res

s = Solution()
print s.kClosest([[1,2],[1,1],[4,3], [0,0]], 1)

