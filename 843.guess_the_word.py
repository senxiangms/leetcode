""" You are given an array of unique strings words where words[i] is six letters long. One word of words was chosen as a secret word.

You are also given the helper object Master. You may call Master.guess(word) where word is a six-letter-long string, and it must be from words. Master.guess(word) returns:

-1 if word is not from words, or
an integer representing the number of exact matches (value and position) of your guess to the secret word.
There is a parameter allowedGuesses for each test case where allowedGuesses is the maximum number of times you can call Master.guess(word).

For each test case, you should call Master.guess with the secret word without exceeding the maximum number of allowed guesses. You will get:

"Either you took too many guesses, or you did not find the secret word." if you called Master.guess more than allowedGuesses times or if you did not call Master.guess with the secret word, or
"You guessed the secret word correctly." if you called Master.guess with the secret word with the number of calls to Master.guess less than or equal to allowedGuesses.
The test cases are generated such that you can guess the secret word with a reasonable strategy (other than using the bruteforce method).

 

Example 1:

Input: secret = "acckzz", words = ["acckzz","ccbazz","eiowzz","abcczz"], allowedGuesses = 10
Output: You guessed the secret word correctly.
Explanation:
master.guess("aaaaaa") returns -1, because "aaaaaa" is not in wordlist.
master.guess("acckzz") returns 6, because "acckzz" is secret and has all 6 matches.
master.guess("ccbazz") returns 3, because "ccbazz" has 3 matches.
master.guess("eiowzz") returns 2, because "eiowzz" has 2 matches.
master.guess("abcczz") returns 4, because "abcczz" has 4 matches.
We made 5 calls to master.guess, and one of them was the secret, so we pass the test case.
Example 2:

Input: secret = "hamada", words = ["hamada","khaled"], allowedGuesses = 10
Output: You guessed the secret word correctly.
Explanation: Since there are two words, you can guess both. """

# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:
#首先求所有词两两比较的匹配字符个数， 得到一个矩阵
#定义函数solve(possible)， possible代表可能集合， 第一次调用是所有词
#对possible集合的每个词， 求和其他词0，1 2.。5个字符相同的个数， 得到最大个数。 比如词A 3个字符相同的次数为100。 词B 两个字符
#相同的次数为120， 从possible集合里选出最大重叠次数最少的那个词（表明字符相同次数0~5分布比较均匀）， 用这个词猜测
#用master.guess的结果得到一个更小的possible集合

import math

class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        N = len(wordlist)
        mp = [[6 for _ in range(N)] for _ in range(N)]
        #assc = defaultdict(int)
        for i in range(N):
            w1 = wordlist[i]
            for j in range(i+1, N):
                w2 = wordlist[j]
                same = 0
                for c1,c2 in zip(w1, w2):
                    if c1 == c2: same+=1
                mp[i][j] = same
                mp[j][i] = same
     
        
        possible = range(N)
        
        def solve(possible):
            mnl = math.inf
            ansguess = None
            if (len(possible) <=2) : 
                return possible[0]
            for guess in possible:
                group =[0 for _ in range(6)]
                for j in possible:
                    if j != guess:
                        group[mp[guess][j]] +=1
                mx = max(group)
                if mnl > mx:
                    mnl = mx
                    ansguess = guess
            return ansguess
                
        while True:
            guess = solve(possible)
            ret = master.guess(wordlist[guess])
            if ret == 6: return wordlist[guess]
            possible = [i for i in possible if mp[guess][i] == ret ]
            
                
                