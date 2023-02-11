import math
""" You have k servers numbered from 0 to k-1 that are being used to handle multiple requests simultaneously. Each server has infinite computational capacity but cannot handle more than one request at a time. The requests are assigned to servers according to a specific algorithm:

The ith (0-indexed) request arrives.
If all servers are busy, the request is dropped (not handled at all).
If the (i % k)th server is available, assign the request to that server.
Otherwise, assign the request to the next available server (wrapping around the list of servers and starting from 0 if necessary). For example, if the ith server is busy, try to assign the request to the (i+1)th server, then the (i+2)th server, and so on.
You are given a strictly increasing array arrival of positive integers, where arrival[i] represents the arrival time of the ith request, and another array load, where load[i] represents the load of the ith request (the time it takes to complete). Your goal is to find the busiest server(s). A server is considered busiest if it handled the most number of requests successfully among all the servers.

Return a list containing the IDs (0-indexed) of the busiest server(s). You may return the IDs in any order.

 Example 1:


Input: k = 3, arrival = [1,2,3,4,5], load = [5,2,3,3,3] 
Output: [1] 
Explanation: 
All of the servers start out available.
The first 3 requests are handled by the first 3 servers in order.
Request 3 comes in. Server 0 is busy, so it's assigned to the next available server, which is 1.
Request 4 comes in. It cannot be handled since all servers are busy, so it is dropped.
Servers 0 and 2 handled one request each, while server 1 handled two requests. Hence server 1 is the busiest server. """

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        #维护两个heap before after， 一个是在当前目标server之前的空闲节点， 一个是之后的空闲节点， 存放空闲节点id
        #维护一个busyjobs堆， 当一个任务来之后， 首先释放所有结束job占用的节点， 堆里存放(jobendtime, node_id)， 
        #释放的空闲节点根据id不同， 放进before或者after
        #在before或者after里选择空闲节点分配
        before=list(range(k))
        after = []
        cnts = [0]*k
        jobs = []
        ans = []
        for i, start in enumerate(arrival):
            time = load[i]
            target = i%k
            if target == 0:
                after = before
                before = []
            while jobs and jobs[0][0] <= start:
                _, free_id = heapq.heappop(jobs)
                if free_id < target:
                    heapq.heappush(before, free_id)
                else:
                    heapq.heappush(after, free_id)
            used_q = after if after else before
            if not used_q:
                continue
            free_id = heapq.heappop(used_q)
            cnts[free_id] +=1
            heapq.heappush(jobs, (start+time, free_id))
        
        mx= -math.inf
        for i, n in enumerate(cnts):
            if n > mx:
                ans = [i]
                mx = n
            elif n == mx:
                ans.append(i)
        return ans