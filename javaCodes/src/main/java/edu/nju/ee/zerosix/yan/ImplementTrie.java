package edu.nju.ee.zerosix.yan;

import java.util.HashMap;

public class ImplementTrie {
    class TrieNode {
        HashMap<Character, TrieNode> children;
        Boolean isEnding;
        public TrieNode(boolean ending) {
            children = new HashMap<>();
            isEnding = ending;
        }
        void setIsEnding(boolean b) {
            isEnding = b;
        }
    }
    class Trie {
        TrieNode root;
        /** Initialize your data structure here. */
        public Trie() {
            root = new TrieNode(false);
        }

        /** Inserts a word into the trie. */
        public void insert(String word) {
            TrieNode curr = root;
            for(int i = 0; i < word.length(); i++) {
                if (i == word.length() - 1) {
                    if (!curr.children.containsKey(word.charAt(i))) {
                        curr.children.put(word.charAt(i), new TrieNode(true));
                    } else {
                        curr.children.get(word.charAt(i)).setIsEnding(true);
                    }
                } else {
                    if (!curr.children.containsKey(word.charAt(i))) {
                        curr.children.put(word.charAt(i), new TrieNode(false));
                    }
                }
                curr = curr.children.get(word.charAt(i));
            }
        }

        /** Returns if the word is in the trie. */
        public boolean search(String word) {
            TrieNode curr = root;
            for (int i = 0; i < word.length(); i++) {
                if (curr.children.containsKey(word.charAt(i))) {
                    curr = curr.children.get(word.charAt(i));
                } else {
                    return  false;
                }
            }
            return curr.isEnding;
        }

        /** Returns if there is any word in the trie that starts with the given prefix. */
        public boolean startsWith(String prefix) {
            TrieNode curr = root;
            for(int i = 0; i < prefix.length(); i++) {
                if (!curr.children.containsKey(prefix.charAt(i))) {
                    return false;
                } else {
                    curr = curr.children.get(prefix.charAt(i));
                }
            }
            return true;
        }
    }

}
