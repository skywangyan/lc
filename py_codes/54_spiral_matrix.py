'''
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix 
in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
'''

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        rowNum = len(matrix)
        colNum = len(matrix[0])
        if not colNum:
            return []
        visited = [[0 for _ in xrange(colNum)] for __ in xrange(rowNum)]
        i, j, res, direction = 0, 0, [], 0
        while 1:
            res.append(matrix[i][j])
            visited[i][j] = 1
            if direction == 0:
                if j + 1 >= colNum or visited[i][j+1]:
                    direction = 1
                    if i+1 >= rowNum or visited[i+1][j]:
                        return res
                    else:
                        i += 1
                else:
                    j += 1
            
            elif direction == 1:
                if i + 1 >= rowNum or visited[i+1][j]:
                    direction = 2
                    if j - 1 < 0 or visited[i][j-1]:
                        return res
                    else:
                        j -= 1
                else:
                    i += 1
            elif direction == 2:
                if j - 1 < 0 or visited[i][j-1]:
                    direction = 3
                    if i - 1 < 0 or visited[i-1][j]:
                        return res
                    else:
                        i -= 1
                else:
                    j -= 1
            elif direction  == 3:
                if i - 1 < 0 or visited[i-1][j]:
                    direction = 0
                    if j + 1 >= colNum or visited[i][j+1]:
                        return res
                    else:
                        j += 1
                else:
                    i -= 1

s = Solution()
print s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
                    
            
