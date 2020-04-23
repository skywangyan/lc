package edu.nju.ee.zerosix.yan;

/*Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

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
        Output: [1,2,3,4,8,12,11,10,9,5,6,7]*/

import java.util.ArrayList;
import java.util.List;

public class SpiralMatrix implements Solution {
    @Override
    public void run() {
        System.out.println(spiralOrder(new int[][]{
                {1,2,3},
                {4,5,6},
                {7,8,9}
        }));
    }
    public List<Integer> spiralOrder(int[][] matrix) {
        int i = 0, j = 0;
        List res = new ArrayList();
        if (matrix.length == 0) {
            return res;
        }
        int rowNum = matrix.length, colNum = matrix[0].length;
        int[] dr = {0, 1, 0, -1};
        int[] dc = {1, 0, -1, 0};
        int direction = 0;
        for (int m = 0; m < rowNum * colNum; m++) {
            res.add(matrix[i][j]);
            matrix[i][j] = Integer.MAX_VALUE;
            int ni = i + dr[direction];
            int nj = j + dc[direction];
            if (0 <= ni && ni < rowNum && 0 <= nj && nj < colNum
                    && matrix[ni][nj] != Integer.MAX_VALUE) {
                i = ni;
                j = nj;
            } else {
                direction = (direction + 1) % 4;
                i += dr[direction];
                j += dc[direction];
            }
        }
        return res;
    }
}
