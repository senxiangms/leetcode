""" You are given an array points, an integer angle, and your location, where location = [posx, posy] and points[i] = [xi, yi] both denote integral coordinates on the X-Y plane.

Initially, you are facing directly east from your position. You cannot move from your position, but you can rotate. In other words, posx and posy cannot be changed. Your field of view in degrees is represented by angle, determining how wide you can see from any given view direction. Let d be the amount in degrees that you rotate counterclockwise. Then, your field of view is the inclusive range of angles [d - angle/2, d + angle/2]. 
You can see some set of points if, for each point, the angle formed by the point, your position, and the immediate east direction from your position is in your field of view.

There can be multiple points at one coordinate. There may be points at your location, and you can always see these points regardless of your rotation. Points do not obstruct your vision to other points.

Return the maximum number of points you can see.

Input: points = [[2,1],[2,2],[3,3]], angle = 90, location = [1,1]
Output: 3
Explanation: The shaded region represents your field of view. All points can be made visible in your field of view, including [3,3] even though [2,2] is in front and in the same line of sight.
Example 2:

Input: points = [[2,1],[2,2],[3,4],[1,1]], angle = 90, location = [1,1]
Output: 4
Explanation: All points can be made visible in your field of view, including the one at your location.


"""
# atan2求相对起始点的角度
#所有点角度排序， 然后对arr + [2pi+ a for a in arr] 进行sliding window
class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        xx, yy = location
        same = 0
        arr = []
        for x, y in points:
            if x == xx and y == yy:
                same+=1
                continue
            arr.append(math.atan2(y-yy, x - xx))
        
        angle = math.pi * angle / 180
        #print(angle)
        arr.sort()
        #print(arr)
        arr = arr + [2*math.pi + a for a in arr]
        #print(arr)
        l = 0
        ret = 0
        for i in range(0, len(arr)):
            while arr[i] - arr[l] > angle:
                l += 1
            ret = max(ret, i-l+1)
        
        return ret + same