""" You are given an integer n, which indicates that there are n courses labeled from 1 to n. You are also given an array relations where relations[i] = [prevCoursei, nextCoursei], representing a prerequisite relationship between course prevCoursei and course nextCoursei: course prevCoursei has to be taken before course nextCoursei. Also, you are given the integer k.

In one semester, you can take at most k courses as long as you have taken all the prerequisites in the previous semesters for the courses you are taking.

Return the minimum number of semesters needed to take all courses. The testcases will be generated such that it is possible to take every course.

 

Example 1: 

Example 1:


Input: n = 4, relations = [[2,1],[3,1],[1,4]], k = 2
Output: 3
Explanation: The figure above represents the given graph.
In the first semester, you can take courses 2 and 3.
In the second semester, you can take course 1.
In the third semester, you can take course 4.


"""

#关键在于当下一学期多余k个课程时， 不同的选择会影响结果， 所以我们要枚举所有可能， 难点
#用bitmask num=1011 表示0, 1, 3课程学过， step表示学期， [0,0]进入队列表示没有可能学过
#mem记录各种已学课程情况下最少需要的学期数。 

from collections import deque
from itertools import combinations
class Solution(object):
    def minNumberOfSemesters(self, n, dependencies, k):
        """
        :type n: int
        :type dependencies: List[List[int]]
        :type k: int
        :rtype: int
        """
        pre = [0]*n
        mem = [20]*(1<<(n))
        for dep in dependencies:
            pre[dep[1]-1] += 1<<(dep[0]-1)
        queue = deque([[0,0]])
        while queue:
            [num,step] = queue.popleft()
            nextlist = []
            for i in range(n):
                if pre[i]&num != pre[i]: continue
                if (1<<i)&num: continue
                nextlist.append(i)     
            if len(nextlist)<=k:
                for ele in nextlist: num += 1<<ele
                if num+1==1<<n: return step+1
                if mem[num]>step+1: 
                    queue.append([num,step+1])
                    mem[num] = step+1
            else:
                thelist = combinations(nextlist,k)
                for seq in thelist:
                    temp = num
                    for ele in list(seq): temp += 1<<ele
                    if mem[temp]>step+1:
                        queue.append([temp,step+1])
                        mem[temp] = step + 1

        
