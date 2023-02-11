""" You are given a binary string s and a positive integer k.

Return the length of the longest subsequence of s that makes up a binary number less than or equal to k.

Note:

The subsequence can contain leading zeroes.
The empty string is considered to be equal to 0.
A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.
 

Example 1:

Input: s = "1001010", k = 5
Output: 5
Explanation: The longest subsequence of s that makes up a binary number less than or equal to 5 is "00010", as this number is equal to 2 in decimal.
Note that "00100" and "00101" are also possible, which are equal to 4 and 5 in decimal, respectively.
The length of this subsequence is 5, so 5 is returned.
Example 2:

Input: s = "00101001", k = 1
Output: 6
Explanation: "000001" is the longest subsequence of s that makes up a binary number less than or equal to 1, as this number is equal to 1 in decimal.
The length of this subsequence is 6, so 6 is returned. """

#如果整体大于等于k， 则返回整个
#否则， 去除最高位的1， 所以我们需要记住最高位的1的位置， 然后每次尝试移去一个最高位的1
class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        total = 0
        N = len(s)
        hp = []
        for i, c in enumerate(s):
            total = total * 2 + ord(c) - ord('0')
            if c == '1':
                hp.append(i)
        if total <= k:
            return N

        i = 0
        while total > k and i < len(hp):
            pos = hp[i]
            total = total - 2**(N-pos-1)
            i+=1
        return N-i