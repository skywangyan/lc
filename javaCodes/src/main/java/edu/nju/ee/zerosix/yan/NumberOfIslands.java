package edu.nju.ee.zerosix.yan;

public class NumberOfIslands {
    public int numIslands(char[][] grid) {
        if (grid.length == 0) {
            return 0;
        }
        int x = grid.length;
        int y = grid[0].length;
        int[][] visited = new int[x][y];
        class Dfs {
            void walk(int r, int c, int[][] v) {
                if(visited[r][c] == 0 && grid[r][c] == '1') {
                    visited[r][c] = 1;
                    if (r+1 < x && grid[r+1][c] == '1') {
                        walk(r+1, c, visited);
                    }
                    if (r-1 >= 0 && grid[r-1][c] == '1') {
                        walk(r-1, c, visited);
                    }
                    if (c+1 < y && grid[r][c+1] == '1') {
                        walk(r, c+1, visited);
                    }
                    if (c-1 >= 0 && grid[r][c-1] == '1') {
                        walk(r,c-1, visited);
                    }
                }
            }
        }
        Dfs d = new Dfs();
        int counter = 0;
        for(int i = 0; i < x; i++) {
            for (int j = 0; j < y; j++) {
                if (grid[i][j] == '1' && visited[i][j] == 0) {
                    d.walk(i,j, visited);
                    counter++;
                }
            }
        }
        return counter;
    }
}
