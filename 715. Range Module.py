""" A Range Module is a module that tracks ranges of numbers. Design a data structure to track the ranges represented as half-open intervals and query about them.

A half-open interval [left, right) denotes all the real numbers x where left <= x < right.

Implement the RangeModule class:

RangeModule() Initializes the object of the data structure.
void addRange(int left, int right) Adds the half-open interval [left, right), tracking every real number in that interval. Adding an interval that partially overlaps with currently tracked numbers should add any numbers in the interval [left, right) that are not already tracked.
boolean queryRange(int left, int right) Returns true if every real number in the interval [left, right) is currently being tracked, and false otherwise.
void removeRange(int left, int right) Stops tracking every real number currently being tracked in the half-open interval [left, right).
Input
["RangeModule", "addRange", "removeRange", "queryRange", "queryRange", "queryRange"]
[[], [10, 20], [14, 16], [10, 14], [13, 15], [16, 17]]
Output
[null, null, null, true, false, true]
Explanation
RangeModule rangeModule = new RangeModule();
rangeModule.addRange(10, 20);
rangeModule.removeRange(14, 16);
rangeModule.queryRange(10, 14); // return True,(Every number in [10, 14) is being tracked)
rangeModule.queryRange(13, 15); // return False,(Numbers like 14, 14.03, 14.17 in [13, 15) are not being tracked)
rangeModule.queryRange(16, 17); // return True, (The number 16 in [16, 17) is still being tracked, despite the remove operation)
  """
#用一个排序list， 插入的时候用bisect找相加的区间， 然后合并更改
#用一个sortedlist， pop掉相交的区间

#或者用一个interval tree, 去除的时候情况太多了。 

from sortedcontainers import SortedList

class RangeModule:

    def __init__(self):
        self.intervals = SortedList()

    def addRange(self, left: int, right: int) -> None:
        k = self.intervals.bisect_left([left, right])
        while k < len(self.intervals) and right >= self.intervals[k][0]: 
            right = max(right, self.intervals[k][1])
            self.intervals.pop(k)
        if k and self.intervals[k-1][1] >= left: 
            left = min(left, self.intervals[k-1][0])
            right = max(right, self.intervals[k-1][1])
            self.intervals.pop(k-1)
        self.intervals.add([left, right])

    def queryRange(self, left: int, right: int) -> bool:
        k = self.intervals.bisect_left([left, right])
        return k and self.intervals[k-1][0] <= left < right <= self.intervals[k-1][1] or k < len(self.intervals) and self.intervals[k][0] <= left < right <= self.intervals[k][1] 

    def removeRange(self, left: int, right: int) -> None:
        k = self.intervals.bisect_left([left, right])
        while k < len(self.intervals) and self.intervals[k][0] <= right: 
            if right < self.intervals[k][1]: 
                self.intervals[k][0] = right 
                break 
            else: self.intervals.pop(k)
        if k and left < self.intervals[k-1][1]: 
            if right < self.intervals[k-1][1]: self.intervals.add([right, self.intervals[k-1][1]])
            self.intervals[k-1][1] = left 



class RangeModule:

    def __init__(self):
        self.ranges = []
    def _bounds(self, left, right):
        lefti = bisect.bisect_left(self.ranges, (left, math.inf))
        righti = bisect.bisect_left(self.ranges, (right, math.inf))
        if lefti-1>=0 and self.ranges[lefti-1][1] >= left:
            i = lefti-1
        else:
            i = lefti
        
        j = righti-1
        return i, j

    def addRange(self, left: int, right: int) -> None:
        i, j = self._bounds(left, right)
        print('add ', left, right, i, j)
        if i > j:
            self.ranges[i:j+1] = [(left, right)]
        else:
            minleft = min(self.ranges[i][0], left)
            maxright = max(self.ranges[j][1], right)
            self.ranges[i:j+1] = [(minleft, maxright)]
        #print('add: ', self.ranges)
        return
        
    def queryRange(self, left: int, right: int) -> bool:
        lefti = bisect.bisect_left(self.ranges, (left, math.inf))
        if lefti: lefti -=1
        if len(self.ranges) == 0: return False
        return self.ranges[lefti][0] <=left<=right<= self.ranges[lefti][1]

        

    def removeRange(self, left: int, right: int) -> None:
        i, j = self._bounds(left, right)
        if i>j: return
        merge=[]
        for x in range(i, j+1):
            if self.ranges[x][0] < left:
                merge.append((self.ranges[x][0], left))
            if self.ranges[x][1] > right:
                merge.append((right, self.ranges[x][1]))
        self.ranges[i:j+1] = merge
        #print('remove :', self.ranges)
        return

# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)
