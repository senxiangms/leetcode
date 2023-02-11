""" Given a rows x cols screen and a sentence represented as a list of strings, return the number of times the given sentence can be fitted on the screen.

The order of words in the sentence must remain unchanged, and a word cannot be split into two lines. A single space must separate two consecutive words in a line.

 

Example 1:

Input: sentence = ["hello","world"], rows = 2, cols = 8
Output: 1
Explanation:
hello---
world---
The character '-' signifies an empty space on the screen.
Example 2:

Input: sentence = ["a", "bcd", "e"], rows = 3, cols = 6
Output: 2
Explanation:
a-bcd- 
e-a---
bcd-e-
The character '-' signifies an empty space on the screen. """
#暴力方法就是对每一行尽可能塞， 塞不下， 换另一行
#用dp方法改进， 不用每次计算第i个词开始一行能填多少个词以及是不是到词表结尾
class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        n = len(sentence)

        @lru_cache(None)
        def dp(i):  # Return (nextIndex, times) if the word at ith is the beginning of the row
            c = 0
            times = 0
            while c + len(sentence[i]) <= cols:
                c += len(sentence[i]) + 1
                i += 1
                if i == n:
                    times += 1
                    i = 0
            return i, times

        ans = 0
        wordIdx = 0
        for _ in range(rows):
            ans += dp(wordIdx)[1]
            wordIdx = dp(wordIdx)[0]
        return ans

        