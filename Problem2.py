# Problem 2 : Word Search
# Time Complexity : O(m*n*3^(l-1))
# Space Complexity : O(l)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this :
'''
None
'''

# Your code here along with comments explaining your approach
from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # length of row and column of board
        row = len(board)
        cols = len(board[0])

        # dfs logic for searching word in the board
        def searchWord(i: int, j: int, index: int) -> bool:
            # base case
            # check if the last character is matching or not
            if index == len(word)-1 :
                return board[i][j] == word[index]
            # check if the character at board[i][j] is not matching with the character at word[index] and it is correct return false
            if board[i][j] != word[index]:
                return False

            # store the current character at board[i][j] position
            temp = board[i][j]
            # marking the board[i][j] position as visited
            board[i][j] = '0'

            # direction array
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            # loop through all four direction
            for dr, dc in directions:
                rr = i + dr
                cc = j + dc
                # check for boundaries and also check if the character at board[i][j] is not visited
                if 0 <= rr < row and 0 <= cc < cols and board[rr][cc] != '0':
                    # recursively call dfs for next character
                    if searchWord(rr, cc, index+1):
                        return True
            # backtrack the change
            board[i][j] = temp
            # if the word is not found then return false
            return False

        # loop through board
        for i in range(row):
            for j in range(cols):
                # check if the first character of word and character at position board[i][j] are equal then call dfs and if dfs also return True then return True
                if board[i][j] == word[0] and searchWord(i, j, 0):
                    return True
        # else return False means word is not search
        return False