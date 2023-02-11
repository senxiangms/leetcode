""" ou are given an array of words where each word consists of lowercase English letters.

wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere in wordA without changing the order of the other characters to make it equal to wordB.

For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad".
A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, where word1 is a predecessor of word2, word2 is a predecessor of word3, and so on. A single word is trivially a word chain with k == 1.

Return the length of the longest possible word chain with words chosen from the given list of words.

 

Example 1:

Input: words = ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: One of the longest word chains is ["a","ba","bda","bdca"].
Example 2:

Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
Output: 5
Explanation: All the words can be put in a word chain ["xb", "xbc", "cxbc", "pcxbc", "pcxbcf"]. """
#首先按字长递增排序， 然后用dp求以当前词结尾的string chain的最大长度， 全局求最大长度dp[i] = dp[j] + 1  j is i-1~0 when word[j] is pred of word[i]

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def ispred(post, prev):
            if len(post) != len(prev)+1: return False
            diff = 0
            i, j = 0, 0
            while i < len(post) and j < len(prev):
                if post[i] != prev[j]: 
                    diff +=1
                    i+=1
                else:
                    i+=1
                    j+=1
            if i != len(post): diff +=1
            ret =  (diff == 1)
            print(post, " ", prev, " return ", ret)
            return ret

        words.sort(key=lambda w: len(w))
        print(words)
        N =len(words)
        dp = [1 for _ in range(N)]
        mx = 1
        for i in range(1, N):
            w = words[i]
            for j in range(i-1, -1, -1):
                if len(words[j])+1 < len(w):
                    break
                if ispred(w, words[j]):
                    dp[i] = max(dp[i], dp[j]+1)
            mx = max(mx, dp[i])
        print(dp)
        return mx
        
                

        return 0