""" Design a phone directory that initially has maxNumbers empty slots that can store numbers. The directory should store numbers, check if a certain slot is empty or not, and empty a given slot.

Implement the PhoneDirectory class:

PhoneDirectory(int maxNumbers) Initializes the phone directory with the number of available slots maxNumbers.
int get() Provides a number that is not assigned to anyone. Returns -1 if no number is available.
bool check(int number) Returns true if the slot number is available and false otherwise.
void release(int number) Recycles or releases the slot number. 

Example 1:

Input
["PhoneDirectory", "get", "get", "check", "get", "check", "release", "check"]
[[3], [], [], [2], [], [2], [2], [2]]
Output
[null, 0, 1, true, 2, false, null, true]

Explanation
PhoneDirectory phoneDirectory = new PhoneDirectory(3);
phoneDirectory.get();      // It can return any available phone number. Here we assume it returns 0.
phoneDirectory.get();      // Assume it returns 1.
phoneDirectory.check(2);   // The number 2 is available, so return true.
phoneDirectory.get();      // It returns 2, the only number that is left.
phoneDirectory.check(2);   // The number 2 is no longer available, so return false.
phoneDirectory.release(2); // Release number 2 back to the pool.
phoneDirectory.check(2);   // Number 2 is available again, return true.

"""
#数组， 每个数组元素包含前节点， 后节点， 空闲标志。 空闲节点串联起来， 形成一个双向链表


from collections import defaultdict, deque

import math
from sortedcontainers import SortedList

class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.arr = [[0, -1, -1] for i in range(maxNumbers)] #occupied, prev, next
        for i in range(maxNumbers):
            if i == 0:
                self.arr[i][2] = (i+1 if i!= maxNumbers-1 else -1)
            elif i == maxNumbers-1:
                self.arr[i][1] = (i-1 if i!= maxNumbers-1 else -1)
            else:
                self.arr[i][2] = i+1
                self.arr[i][1] = i-1
            
        self.free_head = 0


    def get(self) -> int:
        ret = self.free_head
        if self.free_head != -1:
            nxt = self.arr[self.free_head][2]
            if nxt != -1:
                self.arr[nxt][1] = -1
            self.free_head = nxt
            self.arr[ret][0] = 1
        return ret


    def check(self, number: int) -> bool:
        return self.arr[number][0] == 0

    def release(self, number: int) -> None:
        if self.arr[number][0] == 0: return
        
        self.arr[number][0] = 0
        self.arr[number][2] = self.free_head
        self.arr[number][1] = -1
        if self.free_head != -1:
            self.arr[self.free_head][1] = number
        self.free_head = number
        return

cmds = ["PhoneDirectory","release","get","release","release","get","get","check","get","release","get","release","release","get","check","release"]
args = [[3],[2],[],[2],[0],[],[],[1],[],[0],[],[0],[0],[],[1],[1]]
#expected = [null,0,1,true,2,false,null,true]

obj = None
for i, cmd in enumerate(cmds):
    if cmd == "PhoneDirectory":
        obj = PhoneDirectory(args[i][0])
        continue
    if cmd == "get":
        ret = obj.get()
        continue
    if cmd == "release":
        ret = obj.release(args[i][0])
        continue
    if cmd == "check":
        ret = obj.check(args[i][0])
        continue




