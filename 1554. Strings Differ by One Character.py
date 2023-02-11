""" Given a list of strings dict where all the strings are of the same length.

Return true if there are 2 strings that only differ by 1 character in the same index, otherwise return false.

 

Example 1:

Input: dict = ["abcd","acbd", "aacd"]
Output: true
Explanation: Strings "abcd" and "aacd" differ only by one character in the index 1.
Example 2:

Input: dict = ["ab","cd","yz"]
Output: false
Example 3:

Input: dict = ["abcd","cccc","abyd","abab"]
Output: true """

#每个词c2 c1 c0 按c0 + c1*27^1..+ c2*27^2编码， 则c2 c1 * 的编码很容易得到， total-c0*1 .*固定为0， a的编码为1， z为26
class Solution:
    def differByOne(self, dict: List[str]) -> bool:
        
        def hash(s):
            ret = 0
            for c in s:
                ret = ret * 27 + ord(c) - ord('a') + 1
            return ret
        cols = len(dict[0])
        hashes = []
        for w in dict:
            hashes.append(hash(w))

        base = 1
        for x in range(cols-1, -1, -1):
            allmasks = set()
            for i, w in enumerate(dict):    
                L = len(w)
                mask = hashes[i] - (ord(w[x])-ord('a')+1) * base
                
                if mask in allmasks:
                    return True
                else:
                    allmasks.add(mask)
            base = base * 27
        return False
