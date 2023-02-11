""" Your car starts at position 0 and speed +1 on an infinite number line. Your car can go into negative positions. Your car drives automatically according to a sequence of instructions 'A' (accelerate) and 'R' (reverse):

When you get an instruction 'A', your car does the following:
position += speed
speed *= 2
When you get an instruction 'R', your car does the following:
If your speed is positive then speed = -1
otherwise speed = 1
Your position stays the same.
For example, after commands "AAR", your car goes to positions 0 --> 1 --> 3 --> 3, and your speed goes to 1 --> 2 --> 4 --> -1.

Given a target position target, return the length of the shortest sequence of instructions to get there.

 

Example 1:

Input: target = 3
Output: 2
Explanation: 
The shortest instruction sequence is "AA".
Your position goes from 0 --> 1 --> 3.
Example 2:

Input: target = 6
Output: 5
Explanation: 
The shortest instruction sequence is "AAARA".
Your position goes from 0 --> 1 --> 3 --> 7 --> 7 --> 6. """

class Solution:
    def racecar(self, target: int) -> int:
        #仅当下一步超过target的时候， 才进行两种尝试， 掉头或者加速。 
        #bfs
        queue = collections.deque() #moves, pos, speed
        queue.append((0, 0, 1))

        while queue:
            moves, pos, speed = queue.popleft()
            if pos == target:
                return moves
            
            if (pos + speed > target and speed > 0) or (pos + speed < target and speed < 0):
                queue.append((moves+1, pos, 1 if speed < 0 else -1))
            
            queue.append((moves+1, pos + speed, speed*2))
            
            