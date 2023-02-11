""" You are given an m x n matrix board, representing the current state of a crossword puzzle. The crossword contains lowercase English letters (from solved words), ' ' to represent any empty cells, and '#' to represent any blocked cells.

A word can be placed horizontally (left to right or right to left) or vertically (top to bottom or bottom to top) in the board if:

It does not occupy a cell containing the character '#'.
The cell each letter is placed in must either be ' ' (empty) or match the letter already on the board.
There must not be any empty cells ' ' or other lowercase letters directly left or right of the word if the word was placed horizontally.
There must not be any empty cells ' ' or other lowercase letters directly above or below the word if the word was placed vertically.
Given a string word, return true if word can be placed in board, or false otherwise.

Input: board = [["#", " ", "#"], [" ", " ", "#"], ["#", "c", " "]], word = "abc"
Output: true
Explanation: The word "abc" can be placed as shown above (top to bottom). """


#堆每行， 每列， 按# split， 找长度相同并且匹配的段。
class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        R = len(board)
        C = len(board[0])
        def valid(x, y):
            return 0<=x<C and 0<=y<R
        def matched(seg, word):
            succ = True
            for c1, c2 in zip(seg, word):
                if c1 == " " or c1 == c2: 
                    continue
                else:
                    succ = False
                    break
            if succ: 
                print(seg, len(seg), word, succ)
                return succ
            succ = True
            for c1, c2 in zip(seg, word[::-1]):
                if c1 == " " or c1 == c2: 
                    continue
                else:
                    succ = False
                    break
            print(seg, len(seg), word[::-1], succ)
            return succ
        for B in board, zip(*board):
            for row in B:
                s = ''.join(row)
                print(':', s)
                segs = s.split('#')
                print(segs)
                for seg in segs:
                    if len(seg) != len(word):
                        continue
                    elif matched(seg, word):
                        return True
        return False
        