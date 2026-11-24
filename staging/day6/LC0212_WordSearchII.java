import java.util.*;
public class LC0212_WordSearchII {
    static class Trie {
        Trie[] ch = new Trie[26]; String word;
    }
    public List<String> findWords(char[][] board, String[] words) {
        Trie root = new Trie();
        for (String w : words) { Trie cur = root; for (char c : w.toCharArray()) { if (cur.ch[c-'a']==null) cur.ch[c-'a']=new Trie(); cur=cur.ch[c-'a']; } cur.word=w; }
        List<String> res = new ArrayList<>();
        for (int i = 0; i < board.length; i++)
            for (int j = 0; j < board[0].length; j++)
                dfs(board, i, j, root, res);
        return res;
    }
    private void dfs(char[][] b, int i, int j, Trie node, List<String> res) {
        if (i<0||i>=b.length||j<0||j>=b[0].length||b[i][j]=='#') return;
        char c=b[i][j]; if (node.ch[c-'a']==null) return;
        node=node.ch[c-'a']; if (node.word!=null) { res.add(node.word); node.word=null; }
        b[i][j]='#';
        dfs(b,i+1,j,node,res); dfs(b,i-1,j,node,res); dfs(b,i,j+1,node,res); dfs(b,i,j-1,node,res);
        b[i][j]=c;
    }
    public static void main(String[] args) {
        LC0212_WordSearchII sol = new LC0212_WordSearchII();
        char[][] board={{'o','a','a','n'},{'e','t','a','e'},{'i','h','k','r'},{'i','f','l','v'}};
        System.out.println(sol.findWords(board, new String[]{"oath","pea","eat","rain"})); // [eat,oath]
    }
}
