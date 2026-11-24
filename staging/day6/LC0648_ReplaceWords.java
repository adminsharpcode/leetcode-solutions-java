import java.util.*;
public class LC0648_ReplaceWords {
    static class Trie { Trie[] ch = new Trie[26]; String root; }
    public String replaceWords(List<String> dictionary, String sentence) {
        Trie root = new Trie();
        for (String word : dictionary) {
            Trie cur = root;
            for (char c : word.toCharArray()) { if (cur.ch[c-'a']==null) cur.ch[c-'a']=new Trie(); cur=cur.ch[c-'a']; }
            cur.root = word;
        }
        StringBuilder sb = new StringBuilder();
        for (String word : sentence.split(" ")) {
            Trie cur = root; String rep = null;
            for (char c : word.toCharArray()) { if (cur.ch[c-'a']==null || cur.root!=null) { rep=cur.root; break; } cur=cur.ch[c-'a']; }
            if (rep == null) rep = word;
            if (sb.length() > 0) sb.append(' ');
            sb.append(rep);
        }
        return sb.toString();
    }
    public static void main(String[] args) {
        LC0648_ReplaceWords sol = new LC0648_ReplaceWords();
        System.out.println(sol.replaceWords(Arrays.asList("cat","bat","rat"), "the cattle was rattled by the battery"));
        // the cat was rat by the bat
    }
}
