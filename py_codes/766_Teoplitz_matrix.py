# A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.

# Now given an M x N matrix, return True if and only if the matrix is Toeplitz.


# Example 1:

# Input:
# matrix = [
#   [1,2,3,4],
#   [5,1,2,3],
#   [9,5,1,2]
# ]
# Output: True
# Explanation:
# In the above grid, the diagonals are:
# "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
# In each diagonal all elements are the same, so the answer is True.
# Example 2:

# Input:
# matrix = [
#   [1,2],
#   [2,2]
# ]
# Output: False
# Explanation:
# The diagonal "[1, 2]" has different elements.

# Note:

# matrix will be a 2D array of integers.
# matrix will have a number of rows and columns in range [1, 20].
# matrix[i][j] will be integers in range [0, 99].

# Follow up:

# What if the matrix is stored on disk, and the memory is limited such that you can only 
# load at most one row of the matrix into the memory at once?
# What if the matrix is so large that you can only load up a partial row into the memory at 
# once?

class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        width, height = len(matrix[0]), len(matrix)
        for i in xrange(width):
            target = matrix[0][i]
            x, y = 0, i
            while x + 1 < height and y + 1 < width:
                x += 1
                y += 1
                if matrix[x][y] != target:
                    return False
        for j in xrange(height):
            target = matrix[j][0]
            x,y = j,0
            while x + 1 < height and y + 1 < width:
                x += 1
                y += 1
                if matrix[x][y] != target:
                    return False
        return True

    def isToeplitzMatrix2(self, matrix):
        if not matrix:
            return  True
        width, height = len(matrix[0]), len(matrix)
        for i in xrange(width):
            start_value = matrix[0][i]
            m, n = 0, i
            while m < height and n < width:
                if matrix[m][n] != start_value:
                    return False
                m += 1
                n +=1
        for j in xrange(height):
            start_value = matrix[j][0]
            m, n = j, 0
            while m < height and n < width:
                if matrix[m][n] != start_value:
                    return False
                m, n = m+1, n+1
        return True



s = Solution()
print s.isToeplitzMatrix2( [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
])
