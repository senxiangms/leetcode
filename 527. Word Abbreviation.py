""" Given an array of distinct strings words, return the minimal possible abbreviations for every word.

The following are the rules for a string abbreviation:

The initial abbreviation for each word is: the first character, then the number of characters in between, followed by the last character.
If more than one word shares the same abbreviation, then perform the following operation:
Increase the prefix (characters in the first part) of each of their abbreviations by 1.
For example, say you start with the words ["abcdef","abndef"] both initially abbreviated as "a4f". Then, a sequence of operations would be ["a4f","a4f"] -> ["ab3f","ab3f"] -> ["abc2f","abn2f"].
This operation is repeated until every abbreviation is unique.
At the end, if an abbreviation did not make a word shorter, then keep it as the original word.
 

Example 1:

Input: words = ["like","god","internal","me","internet","interval","intension","face","intrusion"]
Output: ["l2e","god","internal","me","i6t","interval","inte4n","f2e","intr4n"]
Example 2:

Input: words = ["aa","aaa"]
Output: ["aa","aaa"] """
#用trie， abcd 建立的节点是"ab": subtrie, 2:+1， 意思是"ab"有个子树， 长度为2的词有一个
#第二步， 如果词长度小于等于3， 则输出。 否认用w[0]+w[-1] 和后续字符搜索trie， 如果节点rest长度为1， compose之后输出， 否则继续搜下一个字符

class Solution:
    def wordsAbbreviation(self, words: List[str]) -> List[str]:
        trie = {}
        for word in words:
            node = trie
            cands = [word[0] + word[-1]] + list(word[1:-1])
            for i, w in enumerate(cands):
                node = node.setdefault(w, {})
                rest = len(cands) - i - 1
                node[rest] = node.get(rest, 0) + 1
        
        print(trie)

        ans = []
        for word in words:
            if len(word) <= 3: 
                ans.append(word)
                continue
            node = trie
            cands = [word[0] + word[-1]] + list(word[1:-1])
            for i, w in enumerate(cands):
                node = node[w]
                rest = len(cands) - i - 1
                if rest > 1 and node[rest] < 2:
                    ans.append(word[:i+1]+str(rest)+word[-1])
                    break
                elif rest <= 1:
                    ans.append(word)
                    break
        
        
        return ans
