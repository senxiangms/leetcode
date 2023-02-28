""" You are given an integer array nums, and you can perform the following operation any number of times on nums:

Swap the positions of two elements nums[i] and nums[j] if gcd(nums[i], nums[j]) > 1 where gcd(nums[i], nums[j]) is the greatest common divisor of nums[i] and nums[j].
Return true if it is possible to sort nums in non-decreasing order using the above swap method, or false otherwise.

 

Example 1:

Input: nums = [7,21,3]
Output: true
Explanation: We can sort [7,21,3] by performing the following operations:
- Swap 7 and 21 because gcd(7,21) = 7. nums = [21,7,3]
- Swap 21 and 3 because gcd(21,3) = 3. nums = [3,7,21]
Example 2:

Input: nums = [5,2,6,2]
Output: false
Explanation: It is impossible to sort the array because 5 cannot be swapped with any other element.
Example 3:

Input: nums = [10,5,9,3,15]
Output: true
We can sort [10,5,9,3,15] by performing the following operations:
- Swap 10 and 15 because gcd(10,15) = 5. nums = [15,5,9,3,10]
- Swap 15 and 3 because gcd(15,3) = 3. nums = [3,5,9,15,10]
- Swap 10 and 15 because gcd(10,15) = 5. nums = [3,5,9,10,15] 
1 <= nums.length <= 3 * 104
2 <= nums[i] <= 105
"""

#因式分解+union find
#对0~10**5 的每个数求最小因子smallest prime factor 对每个i, 遍历j = i*i, i*(i+1)  i*(i+2)都不是质数， spf[j]=min(spf[j], i)
#对每个数， 每个质因子都可以做union find
#对每个nums和sorted(nums)的数对， 如果他们不在一个连通里面， 显然不能做到
class UnionFind:
    def __init__(self):
        self.parent = {}

    def find(self, u):
        if u != self.parent.setdefault(u, u):
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu != pv: self.parent[pu] = pv


class Solution:
    def gcdSort(self, nums: List[int]) -> bool:
        def sieve(n):  # O(N*log(logN)) ~ O(N)
            spf = [i for i in range(n)]
            for i in range(2, n):
                if spf[i] != i: continue  # Skip if it's a not prime number
                for j in range(i * i, n, i):
                    if spf[j] > i:  # update to the smallest prime factor of j
                        spf[j] = i
            return spf

        def getPrimeFactors(num, spf):  # O(logNum)
            while num > 1:
                yield spf[num]
                num //= spf[num]

        spf = sieve(max(nums) + 1)
        uf = UnionFind()
        for x in nums:
            for f in getPrimeFactors(x, spf):
                uf.union(x, f)

        for x, y in zip(nums, sorted(nums)):
            if uf.find(x) != uf.find(y):
                return False

        return True