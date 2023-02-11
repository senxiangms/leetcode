""" We can use run-length encoding (i.e., RLE) to encode a sequence of integers. In a run-length encoded array of even length encoding (0-indexed), for all even i, encoding[i] tells us the number of times that the non-negative integer value encoding[i + 1] is repeated in the sequence.

For example, the sequence arr = [8,8,8,5,5] can be encoded to be encoding = [3,8,2,5]. encoding = [3,8,0,9,2,5] and encoding = [2,8,1,8,2,5] are also valid RLE of arr.
Given a run-length encoded array, design an iterator that iterates through it.

Implement the RLEIterator class:

RLEIterator(int[] encoded) Initializes the object with the encoded array encoded.
int next(int n) Exhausts the next n elements and returns the last element exhausted in this way. If there is no element left to exhaust, return -1 instead.

Input
["RLEIterator", "next", "next", "next", "next"]
[[[3, 8, 0, 9, 2, 5]], [2], [1], [1], [2]]
Output
[null, 8, 8, 5, -1]
 """

 #没有难度， 花时间理解题目， 用指针往后移， 维护好变量。 

 class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.encoding= encoding
        self.cur = 0
        self.cur_used = 0

    def next(self, n: int) -> int:
        
        while self.cur < len(self.encoding)-1:
            if self.cur_used < self.encoding[self.cur]:
                left = self.encoding[self.cur] - self.cur_used
                if left >= n:
                    self.cur_used += n
                    return self.encoding[self.cur+1]
                else:
                    self.cur+=2
                    self.cur_used = 0
                    n-=left
            else:
                self.cur+=2
                self.cur_used = 0
        return -1