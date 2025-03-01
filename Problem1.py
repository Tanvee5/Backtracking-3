# Problem 1 : N-Queens
# Time Complexity : O(n*n!)
# Space Complexity : O(n*n!)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this :
'''
None
'''

# Your code here along with comments explaining your approach
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        solutions = []
        booleanBoard= [[False] * n for _ in range(n)]
        def isSafe(board: List[List[bool]], row: int, col: int) -> bool:
            for i in range(row):
                if board[i][col]:
                    return False
            i = row
            j = col
            while i >= 0 and j >= 0:
                if board[i][j]:
                    return False
                i -= 1
                j -= 1

            i = row
            j = col
            while i >= 0 and j < len(board[0]):
                if board[i][j]:
                    return False
                i -= 1
                j += 1
            
            return True



        def backtrack(board: List[List[bool]], row: int, solution: List[str]) -> None:
            # base case
            
            if row == len(board):
                solutionrow = []
                
                # print(board)
                for i in range(len(board)):
                    solutionsubstring = ""
                    for j in range(len(board[0])):
                        # print("I:", board[i][j])
                        if (board[i][j]):
                            solutionsubstring += "Q"
                            # print("Reached inside:", solutionsubstring)
                        else:
                            solutionsubstring += "."
                    # print("break", solutionsubstring)
                    solutionrow.append(solutionsubstring)
                # print("break", solutionrow)
                solutions.append(solutionrow)


            # logic 
            for col in range(n):
                # print(isSafe(board, row, col))
                if (isSafe(board, row, col)):
                    board[row][col] = True
                    backtrack(board, row+1, solution)
                    board[row][col] = False

        backtrack(booleanBoard, 0, [])
        return solutions