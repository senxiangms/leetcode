""" You are given an integer n. There are n rooms numbered from 0 to n - 1.

You are given a 2D integer array meetings where meetings[i] = [starti, endi] means that a meeting will be held during the half-closed time interval [starti, endi). All the values of starti are unique.

Meetings are allocated to rooms in the following manner:

Each meeting will take place in the unused room with the lowest number.
If there are no available rooms, the meeting will be delayed until a room becomes free. The delayed meeting should have the same duration as the original meeting.
When a room becomes unused, meetings that have an earlier original start time should be given the room.
Return the number of the room that held the most meetings. If there are multiple rooms, return the room with the lowest number.

A half-closed interval [a, b) is the interval between a and b including a and not including b.

 

Example 1:

Input: n = 2, meetings = [[0,10],[1,5],[2,7],[3,4]]
Output: 0
Explanation:
- At time 0, both rooms are not being used. The first meeting starts in room 0.
- At time 1, only room 1 is not being used. The second meeting starts in room 1.
- At time 2, both rooms are being used. The third meeting is delayed.
- At time 3, both rooms are being used. The fourth meeting is delayed.
- At time 5, the meeting in room 1 finishes. The third meeting starts in room 1 for the time period [5,10).
- At time 10, the meetings in both rooms finish. The fourth meeting starts in room 0 for the time period [10,11).
Both rooms 0 and 1 held 2 meetings, so we return 0.  """

# meeting 排序， 维护一个空闲会议室堆， 值为编号， 一个会议堆， 结束时间最小的在堆顶
#每次新会议来， 要把进行的会议看是否已经结束， 如果结束， 释放会议室
#如果有空闲会议室， 则分配最小编号
#如果没有， 结束最早的一个会议， 并更改当前会议的结束时间
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        hp_end = [] #end time, i
        arr = [0 for _ in range(n)]
        hp_room = [i for i in range(n)]

        i = 0
        while i < len(meetings):
            start, end = meetings[i]
            while len(hp_end) != 0 and hp_end[0][0] <= start:
                
                _, release_i = heapq.heappop(hp_end)
                heapq.heappush(hp_room, release_i)
                
            if len(hp_room):
                id = heapq.heappop(hp_room)
                arr[id] +=1
                heapq.heappush(hp_end, (end, id))
                #print(id, " assigned")
                #print(hp_end)

            else:
                #print(hp_end, " empty")
                endtime, room_i = heapq.heappop(hp_end)
                #print(endtime, room_i, " finished")
                arr[room_i] +=1
                
                newstart = endtime
                newend = endtime + end - start
                heapq.heappush(hp_end, (newend, room_i))
                    
            i+=1
        max_i = 0
        mx = -math.inf
        print(arr)
        for i, n in enumerate(arr):
            if n > mx:
                max_i = i
                mx = n
        return max_i