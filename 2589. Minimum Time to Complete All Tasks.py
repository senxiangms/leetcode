""" 2589. Minimum Time to Complete All Tasks
Hard
17
2
There is a computer that can run an unlimited number of tasks at the same time. You are given a 2D integer array tasks where tasks[i] = [starti, endi, durationi] indicates that the ith task should run for a total of durationi seconds (not necessarily continuous) within the inclusive time range [starti, endi].

You may turn on the computer only when it needs to run a task. You can also turn it off if it is idle.

Return the minimum time during which the computer should be turned on to complete all tasks.

 

Example 1:

Input: tasks = [[2,3,1],[4,5,1],[1,5,2]]
Output: 2
Explanation: 
- The first task can be run in the inclusive time range [2, 2].
- The second task can be run in the inclusive time range [5, 5].
- The third task can be run in the two inclusive time ranges [2, 2] and [5, 5].
The computer will be on for a total of 2 seconds.
Example 2:

Input: tasks = [[1,3,2],[2,5,3],[5,6,2]]
Output: 4
Explanation: 
- The first task can be run in the inclusive time range [2, 3].
- The second task can be run in the inclusive time ranges [2, 3] and [5, 5].
- The third task can be run in the two inclusive time range [5, 6].
The computer will be on for a total of 4 seconds. """

#前提是时间限制在2001
#用timeline做， 首先按结束时间排序， 这样可以尽量使用靠近end的时间点去开机。 如果用起始时间排序， 则没法贪心。 
class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        tasks.sort(key= lambda x: x[1])
        print(tasks)
        timeline=[0] * 2001
        ans = 0
        for s, e, d in tasks:
            for t in range(s, e+1):
                if d == 0: break
                if timeline[t] == 1:
                    d-=1
            for i in range(e, s-1, -1):
                if d == 0: break
                if timeline[i] == 0:
                    ans+=1
                    timeline[i] = 1
                    d-=1
        return sum(timeline)