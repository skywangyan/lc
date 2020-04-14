package edu.nju.ee.zerosix.yan;

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

/*
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

        For example, given n = 3, a solution set is:

        [
        "((()))",
        "(()())",
        "(())()",
        "()(())",
        "()()()"
        ]
*/
public class GenerateParentheses implements Solution {
    @Override
    public void run(){
        System.out.println(generateParenthesis(3));
    }

    public List<String> generateParenthesis(int n) {
        ArrayList<String> output = new ArrayList<String>();
        backTracking("", new Stack<String>(), n*2, output);
        return  output;
    }

    private void backTracking(String sofar, Stack<String> reduced, int targetLenth, ArrayList<String> output) {
        if (sofar.length() == targetLenth) {
            if (reduced.empty()) output.add(sofar);
            return;
        }

        if (reduced.empty()) {
            Stack<String> nextReduce = (Stack<String>) reduced.clone();
            nextReduce.push("(");
            backTracking(sofar+"(", nextReduce, targetLenth, output);
        }
        else {
            Stack<String> nextReduce1 = (Stack<String>) reduced.clone();
            nextReduce1.push("(");
            backTracking(sofar+"(", nextReduce1, targetLenth, output);

            Stack<String> nextReduce2 = (Stack<String>) reduced.clone();
            nextReduce2.pop();
            backTracking(sofar+")", nextReduce2, targetLenth, output);

        }

    }
}
