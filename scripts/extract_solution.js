const fs = require('fs');
const path = require('path');

function extractLeetCodeSnippet(javaFilePath) {
  let content = fs.readFileSync(javaFilePath, 'utf8');

  // Extract link
  const linkMatch = content.match(/Link:\s*(https:\/\/leetcode\.com\/problems\/[a-zA-Z0-9-]+\/)/);
  const url = linkMatch ? linkMatch[1] : null;

  // Extract title & number
  const titleMatch = content.match(/LeetCode\s*(\d+):\s*(.+)/);
  const problemNumber = titleMatch ? titleMatch[1] : null;
  const problemTitle = titleMatch ? titleMatch[2].trim() : null;

  // 1. Remove public static class ListNode { ... }
  content = content.replace(/public\s+static\s+class\s+ListNode\s*\{[\s\S]*?\n\s*\}\n/g, '');
  // 2. Remove public static class TreeNode { ... }
  content = content.replace(/public\s+static\s+class\s+TreeNode\s*\{[\s\S]*?\n\s*\}\n/g, '');

  // 3. Remove main method block
  content = content.replace(/public\s+static\s+void\s+main\s*\([^)]*\)\s*\{[\s\S]*?\n\s*\}\s*\n\}/g, '}');

  // 4. Change `public class LCXXXX...` to `class Solution` (except for LC0208 which is Trie design)
  if (path.basename(javaFilePath).includes('LC0208_ImplementTrie')) {
    content = content.replace(/public\s+class\s+LC0208_ImplementTrie\s*\{/, 'class Trie {');
  } else {
    content = content.replace(/public\s+class\s+LC\d+_[a-zA-Z0-9_]+\s*\{/, 'class Solution {');
  }

  return {
    url,
    problemNumber,
    problemTitle,
    code: content.trim()
  };
}

module.exports = { extractLeetCodeSnippet };

if (require.main === module) {
  const testFile = 'E:/LeetCode-Solutions-Java/LC0019_RemoveNthNodeFromEndOfList.java';
  console.log(extractLeetCodeSnippet(testFile));
}
