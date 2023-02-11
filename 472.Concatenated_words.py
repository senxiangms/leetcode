""" Given an array of strings words (without duplicates), return all the concatenated words in the given list of words.

A concatenated word is defined as a string that is comprised entirely of at least two shorter words (not necesssarily distinct) in the given array.

 

Example 1:

Input: words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats"; 
"dogcatsdog" can be concatenated by "dog", "cats" and "dog"; 
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
Example 2:

Input: words = ["cat","dog","catdog"]
Output: ["catdog"] """


import collections

class Solution:
    def findAllConcatenatedWordsInADict(self, words) :
        maxlen = max([len(w) for w in words])
        minlen = min([len(w) for w in words])
        
        dic = set(words)
        
        def CatNum(ss, start):
            if start in mem:
                return mem[start]
            if start == len(ss):
                return 0
            L = len(ss)
            for l in range(minlen, maxlen+1):
                if start + l <= L and ss[start:start+l] in dic:
                    nxt = CatNum(ss, start+l)
                    if nxt >= 0:
                        mem[start] = 1 + nxt
                        return 1+nxt
            mem[start] = -1

            return -1
        ret = []
        for w in words:
            mem = collections.defaultdict(int)
            res = CatNum(w, 0)
            if res > 1:
                ret.append(w)
        return ret

words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
sol = Solution()
sol.findAllConcatenatedWordsInADict(words)