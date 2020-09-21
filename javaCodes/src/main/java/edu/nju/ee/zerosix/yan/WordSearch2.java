package edu.nju.ee.zerosix.yan;

import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;

public class WordSearch2 {
    class TrieNode {
        HashMap<Character, TrieNode> children;
        boolean isEnd;
        public TrieNode(boolean b){
            isEnd = b;
            children = new HashMap<Character, TrieNode>();
        }
        public void setIsEnd(boolean b) {
            isEnd = b;
        }
    }

    TrieNode root = new TrieNode(false);
    List<String> res = new LinkedList<>();

    public void buildTrie(String[] words){
        for(String word : words) {
            TrieNode curr = root;
            for(int i = 0; i < word.length(); i++){
                if (curr.children.containsKey(word.charAt(i))){
                    curr = curr.children.get(word.charAt(i));
                    if (i == word.length() - 1) {
                        curr.setIsEnd(true);
                    }
                } else {
                    if (i != word.length() - 1) {
                        curr.children.put(word.charAt(i), new TrieNode(false));
                    } else {
                        curr.children.put(word.charAt(i), new TrieNode(true));
                    }
                    curr = curr.children.get(word.charAt(i));
                }
            }
        }
    }

    public List<String> findWords(char[][] board, String[] words) {
        buildTrie(words);
        if(board.length == 0) return new LinkedList<>();
        int[][] visited = new int[board.length][board[0].length];
        class DFS {
            public void backTrack(String prev, int row, int col, TrieNode curr) {
                if (visited[row][col] == 0) {
                    char currGrid = board[row][col];
                    if (curr.children.containsKey(currGrid)){
                        visited[row][col] = 1;
                        TrieNode nextTrie = curr.children.get(currGrid);
                        if (nextTrie.isEnd) {
                            String oneWord = prev + currGrid;
                            if (!res.contains(oneWord)){
                                res.add(oneWord);
                            }
                        }
                        if (row > 0) backTrack(prev + currGrid, row-1, col, nextTrie);
                        if (row < board.length - 1) backTrack(prev + currGrid, row + 1, col, nextTrie);
                        if (col > 0) backTrack(prev + currGrid, row, col - 1, nextTrie);
                        if (col < board[0].length - 1) backTrack(prev + currGrid, row, col + 1, nextTrie);
                        //restore
                        visited[row][col] = 0;
                    }
                }
            }
        }
        DFS dfs = new DFS();
        for(int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++){
                dfs.backTrack("", i, j, root);
            }
        }
        return res;
    }
}
