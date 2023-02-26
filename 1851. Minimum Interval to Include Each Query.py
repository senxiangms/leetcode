""" You are given a 2D integer array intervals, where intervals[i] = [lefti, righti] describes the ith interval starting at lefti and ending at righti (inclusive). The size of an interval is defined as the number of integers it contains, or more formally righti - lefti + 1.

You are also given an integer array queries. The answer to the jth query is the size of the smallest interval i such that lefti <= queries[j] <= righti. If no such interval exists, the answer is -1.

Return an array containing the answers to the queries.

 

Example 1:

Input: intervals = [[1,4],[2,4],[3,6],[4,4]], queries = [2,3,4,5]
Output: [3,3,1,4]
Explanation: The queries are processed as follows:
- Query = 2: The interval [2,4] is the smallest interval containing 2. The answer is 4 - 2 + 1 = 3.
- Query = 3: The interval [2,4] is the smallest interval containing 3. The answer is 4 - 2 + 1 = 3.
- Query = 4: The interval [4,4] is the smallest interval containing 4. The answer is 4 - 4 + 1 = 1.
- Query = 5: The interval [3,6] is the smallest interval containing 5. The answer is 6 - 3 + 1 = 4.
Example 2:

Input: intervals = [[2,3],[2,5],[1,8],[20,25]], queries = [2,19,5,22]
Output: [2,-1,4,6]
Explanation: The queries are processed as follows:
- Query = 2: The interval [2,3] is the smallest interval containing 2. The answer is 3 - 2 + 1 = 2.
- Query = 19: None of the intervals contain 19. The answer is -1.
- Query = 5: The interval [2,5] is the smallest interval containing 5. The answer is 5 - 2 + 1 = 4.
- Query = 22: The interval [20,25] is the smallest interval containing 22. The answer is 25 - 20 + 1 = 6. """
#区间排序， query 排序
#对每一个query， 1. 把所有起始点小于query的区间进堆， 堆顶为size最小的区间， 2. 把结束点小于query的区间都pop出来，这些区间
# 都不可能包含接下来的q，  则留下的堆顶区间就是最小包含区间。 


import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals = sorted(intervals)
        queries = sorted([(val, i) for i, val in enumerate(queries) ] )

        print(intervals)
        print(queries)

        hp = []
        ans = [-1 for _ in range(len(queries))]
        
        iInt = 0
        
        for val, i in queries:
            
            while iInt < len(intervals) and intervals[iInt][0] <= val:
                size = intervals[iInt][1] - intervals[iInt][0] + 1
                heapq.heappush(hp, (size, intervals[iInt]))
                iInt+=1
            
            while hp and hp[0][1][1] < val:
                heapq.heappop(hp)
            
            if len(hp) > 0:
                ans[i] = hp[0][0]

        return ans
