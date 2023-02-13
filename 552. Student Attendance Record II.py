""" An attendance record for a student can be represented as a string where each character signifies whether the student was absent, late, or present on that day. The record only contains the following three characters:

'A': Absent.
'L': Late.
'P': Present.
Any student is eligible for an attendance award if they meet both of the following criteria:

The student was absent ('A') for strictly fewer than 2 days total.
The student was never late ('L') for 3 or more consecutive days.
Given an integer n, return the number of possible attendance records of length n that make a student eligible for an attendance award. The answer may be very large, so return it modulo 109 + 7.

 

Example 1:

Input: n = 2
Output: 8
Explanation: There are 8 records with length 2 that are eligible for an award:
"PP", "AP", "PA", "LP", "PL", "AL", "LA", "LL"
Only "AA" is not eligible because there are 2 absences (there need to be fewer than 2). """

import numpy as np

class Solution:
    def checkRecord(self, n: int) -> int:
        MODULUS = 10**9 + 7

        initial_counts = np.array(
            [1, 0, 0, 0, 0, 0], 
            dtype=np.int64
        )

        adjacency_matrix = np.array([
            [1, 1, 1, 0, 0, 0],
            [1, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1],
            [0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0],
        ], dtype=np.int64)

        def power(A, exp):
            B = np.identity(len(A), dtype=np.int64)
            for bit in reversed(bin(exp)[2:]):
                if bit == '1':
                    B = B @ A
                    B %= MODULUS
                A = A @ A
                A %= MODULUS
            return B

        final_counts = power(adjacency_matrix, n) @ initial_counts

        return sum(final_counts) % MODULUS

        
        
        #slow
        self.ans = 0
        mem=collections.defaultdict()
        def rec(start, conse, abtotal):
            
            if start == n:
                return 1
            ans = 0
            if abtotal <=0 :
                
                ans += rec(start+1, conse, abtotal+1)
                
            if conse<=1:
                
                ans += rec(start+1, conse+1, abtotal)
                

            
            ans += rec(start+1, conse, abtotal)
            mem[start, conse, abtotal] = ans
            return ans
            

        ret = rec(0, 0, 0)
        return ret % (10**9+7)

