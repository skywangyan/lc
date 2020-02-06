package edu.nju.ee.zerosix.yan;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class LetterCombinationPhoneNumber implements Solution {
    @Override
    public void run() {
        letterCombinations("234").forEach(x -> System.out.println(x));
    }

    public List<String> letterCombinations(String digits) {
        Map<String, String> map = new HashMap<String, String>();
        map.put("2", "abc");
        map.put("3", "def");
        map.put("4", "ghi");
        map.put("5", "jkl");
        map.put("6", "mno");
        map.put("7", "pqrs");
        map.put("8", "tuv");
        map.put("9", "wxyz");

        int length = digits.length();

        class DFS {
            ArrayList<String> dfs(int startIndex, ArrayList<String> soFar) {
                if (startIndex == length) return soFar;
                ArrayList<String> next = new ArrayList<String>();
                String tmp = map.get(digits.substring(startIndex, startIndex + 1));
                if (!soFar.isEmpty()) {
                    soFar.forEach(x -> {
                        for (int i = 0; i < tmp.length(); i++) {
                            next.add(x + tmp.substring(i, i + 1));
                        }
                    });
                } else {
                    for(char c : tmp.toCharArray()) {
                        next.add(Character.toString(c));
                    }
                }
                return dfs(startIndex + 1, next);
            }
        }
        DFS dfstrack = new DFS();
        ArrayList<String> start = new ArrayList<String>();
        return dfstrack.dfs(0, start);
    }
}

