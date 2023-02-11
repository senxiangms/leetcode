""" Given an array of digits digits, return the largest multiple of three that can be formed by concatenating some of the given digits in any order. If there is no answer return an empty string.

Since the answer may not fit in an integer data type, return the answer as a string. Note that the returning answer must not contain unnecessary leading zeros.

Example 1:

Input: digits = [8,1,9]
Output: "981"
Example 2:

Input: digits = [8,6,7,1,0]
Output: "8760"
Example 3:

Input: digits = [1]
Output: "" """
#如果total sum被三整除， 不用去除数字。 如果余1，2， 去除余数为1和2的数字。 如果不能去除一个数字， 则去除两个数字。 

class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        def trim_0(s):
            if s == "": return s
            ret = s.lstrip('0')
            return ret if len(ret) >0 else '0'

        total = sum(digits)
        if total % 3 == 0:
            result = sorted(digits, reverse=True)
            
            ret = [str(x) for x in result]
            return  trim_0(''.join(ret))

        lefts = [(n % 3, n) for n in digits]
        dic=collections.defaultdict(list)
        for l, n in lefts:
            dic[l].append(n)
        target = total%3
        if target in dic:
            mn = min(dic[target])
            result = sorted(digits, reverse=True)
            ret = []
            first = True
            for x in result:
                if x == mn and first:
                    first = False
                    continue
                ret.append(str(x))
            return trim_0(''.join(ret))
        if target == 1:
            target =2 # find two 2
        else:
            target = 1 #find two 1

        if target not in dic:
            return ""
        if len(dic[target]) < 2:
            return ""

        
        targets = sorted(dic[target])
        removed = targets[0:2]
        result = sorted(digits, reverse=True)
        skip = 0
        print(removed)
        ret = []
        for x in digits:
            if skip < 2 and x == removed[0] or x == removed[1]:
                skip+=1
            else:
                ret.append(str(x))
        return trim_0(''.join(ret))
            



