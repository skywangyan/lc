package edu.nju.ee.zerosix.yan;

import org.junit.Test;

import java.util.List;

public class LeetCodeTest {
    @Test
    public void nextPermutationTest(){
        NextPermutation np = new NextPermutation();
        np.run();
    }


    @Test()
    public void TrappingRainWaterTest(){
        TrappingRainWater trw = new TrappingRainWater();
        trw.run();
    }

    @Test
    public void WildcardMatchingTest(){
        WildcardMatching wm = new WildcardMatching();
        wm.run();
    }

    @Test
    public void powTest(){
        Pow p = new Pow();
        p.run();
    }

    @Test
    public void spiralMatrix(){
        SpiralMatrix sm = new SpiralMatrix();
        sm.run();
    }

    @Test
    public void mergeIntervals(){
        MergeIntervals mi = new MergeIntervals();
        mi.run();
    }

    @Test
    public void insertInterval(){
        InsertInterval ii = new InsertInterval();
        ii.run();
    }

    @Test
    public void plusOne(){
        PlusOne po = new PlusOne();
        po.run();
    }

    @Test
    public void longestConsecutiveSequence(){
        LongestConsecutiveSequence lcs = new LongestConsecutiveSequence();
        lcs.run();
    }

    @Test
    public void cloneGraph(){
        CloneGraph cg = new CloneGraph();
        cg.run();
    }

    @Test
    public void wordBreak(){
        WordBreak wb = new WordBreak();
        wb.run();
    }

    @Test
    public void wordBreakII() {
        WordBreakII wdii = new WordBreakII();
        wdii.run();
    }

    @Test
    public void LRUCache(){
        LRUCache cache = new LRUCache(2);
        cache.run();
    }

    @Test
    public void minStack() {
        MinStack ms = new MinStack();
        ms.run();
    }

    @Test
    public void findPeakElement(){
        FindPeakElement fpe = new FindPeakElement();
        fpe.run();
    }

    @Test
    public void fractionToRecurringDecimal(){
        FractionToRecurringDecimal ftrd = new FractionToRecurringDecimal();
        ftrd.run();
    }

    @Test
    public void binarySearchTreeIterator(){
        BinarySearchTreeIterator bstIt = new BinarySearchTreeIterator();
        bstIt.run();
    }

    @Test
    public void numberOfIslands() {
        NumberOfIslands noi = new NumberOfIslands();
        char[][] input = new char[][]{
                {'1','1','0','0','0'},
                {'1','1','0','0','0'},
                {'0','0','1','0','0'},
                {'0','0','0','1','1'}
        };
        System.out.println(noi.numIslands(input));
    }

    @Test
    public void implementTrie(){
        ImplementTrie it = new ImplementTrie();
        ImplementTrie.Trie t = it.new Trie();
        t.insert("hello");
        assert(t.search("he") == false);
        assert (t.startsWith("he") == true);
        assert (t.search("hello") == true);
    }

    @Test
    public void wordSearch2(){
        WordSearch2 ws2 = new WordSearch2();
        char[][] board = {
                {'o','a','a','n'},
                {'e','t','a','e'},
                {'i','h','k','r'},
                {'i','f','l','v'}
        };
        String[] words = {"oath","pea","eat","rain"};
        List<String> ans1 = ws2.findWords(board, words);
        assert (ans1.size() == 2);

    }

    @Test
    public void shortestPalindrome(){
        ShortestPalindrome sp = new ShortestPalindrome();
        System.out.println(sp.shortestPalindrome(""));
    }

    @Test
    public void theSkylineProblem(){
        TheSkylineProblem tsp = new TheSkylineProblem();
        int[][] builds = {
                {2,9,10},
                {3,7,15},
                {5,12,12},
                {15,20,10},
                {19,24,8}
        };
        System.out.println(tsp.getSkyline(builds));
    }

    @Test
    public void basicCalculator(){
        BasicCalculator bc = new BasicCalculator();
        System.out.println(bc.calculate("((3-4)-(1+2))"));
    }

    @Test
    public void summaryRanges(){
        SummaryRanges sr = new SummaryRanges();
        int[] x = new int[]{-1};
        System.out.println(sr.summaryRanges(x));
    }

    @Test
    public void kthSmallestElementInBST(){
        TreeNode root = new TreeNode(5);
        root.left = new TreeNode(4);
        root.right = new TreeNode(6);
        KthSmallestElementInBST kseibst = new KthSmallestElementInBST();
        System.out.println(kseibst.kthSmallest(root, 1));
    }
}
