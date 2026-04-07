class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row without duplicates
        for row in range(9):
            r = [] 
            for col in range(9):
                if board[row][col] == '.':
                    continue
                if board[row][col] in r:
                    print(f"here r: {r} board[row][col] {board[row][col]}")
                    return False
                r.append(board[row][col])

        # col wothout duplicates
        for col in range(9):
            c = []
            for row in range(9):
                if board[row][col] == '.':
                    continue
                if board[row][col] in c:
                    return False
                c.append(board[row][col])

        for boxes in range(9):
            b = []
            for i in range(3):
                for j in range(3):
                    
                    row = (boxes//3)*3 + i
                    col = (boxes%3)*3 + j
                    if board[row][col] == '.':
                        continue
                    if board[row][col] in b:
                        return False
                    b.append(board[row][col])
        return True

"""
# box = 0
r = (0,1,2//3) * 3 + 0,1,2 = 0,1,2
c = (0,1,2%3) * 3 + 0,1,2 = 0,3,6


r= (0//3)*3+0
c= (0%3)*3+0
c= (0%3)*3+1
c= (0%3)*3+2

r= (0//3)*3+1
c= (0%3)*3+0
c= (0%3)*3+1
c= (0%3)*3+2

r= (0//3)*3+2
c= (0%3)*3+0
c= (0%3)*3+1
c= (0%3)*3+2

r= (1//3)*3+0= 0
c= (1%3)*3+0= 3
c= (1%3)*3+1= 4
c= (1%3)*3+2= 5
"""