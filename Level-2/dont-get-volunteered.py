# Don't Get Volunteered!
# ======================

# As a henchman on Commander Lambda's space station, you're expected to be resourceful, smart, and a quick thinker. 
# It's not easy building a doomsday device and ordering the bunnies around at the same time, after all! In order to make sure 
# that everyone is sufficiently quick-witted, Commander Lambda has installed new flooring outside the henchman dormitories. 
# It looks like a chessboard, and every morning and evening you have to solve a new movement puzzle in order to cross the floor. 
# That would be fine if you got to be the rook or the queen, but instead, you have to be the knight. Worse, if you take too much time solving the puzzle, 
# you get "volunteered" as a test subject for the LAMBCHOP doomsday device!

# To help yourself get to and from your bunk every day, write a function called solution(src, dest) which takes in two parameters: 
# the source square, on which you start, and the destination square, which is where you need to land to solve the puzzle.  
# The function should return an integer representing the smallest number of moves it will take for you to travel from the source square to the destination 
# square using a chess knight's moves (that is, two squares in any direction immediately followed by one square perpendicular to that direction, or vice versa, 
# in an "L" shape).  Both the source and destination squares will be an integer between 0 and 63, inclusive, and are numbered like the example chessboard below:

# -------------------------
# | 0| 1| 2| 3| 4| 5| 6| 7|
# -------------------------
# | 8| 9|10|11|12|13|14|15|
# -------------------------
# |16|17|18|19|20|21|22|23|
# -------------------------
# |24|25|26|27|28|29|30|31|
# -------------------------
# |32|33|34|35|36|37|38|39|
# -------------------------
# |40|41|42|43|44|45|46|47|
# -------------------------
# |48|49|50|51|52|53|54|55|
# -------------------------
# |56|57|58|59|60|61|62|63|
# -------------------------

# Languages
# =========

# To provide a Python solution, edit solution.py
# To provide a Java solution, edit Solution.java

# Test cases
# ==========
# Your code should pass the following test cases.
# Note that it may also be run against hidden test cases not shown here.

# -- Python cases --
# Input:
# solution.solution(0, 1)
# Output:
#     3

# Input:
# solution.solution(19, 36)
# Output:
#     1

# -- Java cases --
# Input:
# Solution.solution(19, 36)
# Output:
#     1

# Input:
# Solution.solution(0, 1)
# Output:
#     3


from collections import deque

#func to build the chessboard.

def solution(src, dest):
    def generate_board():
        i,j = (0,0)
        row, column = (7,7)
        value = 0
        board = []

        #generate the chessboard
        for i in range(row + 1):
            col =[]
            for j in range(column+1):
                col.append(value)
                value += 1
            board.append(col)
    
        return board

    board = generate_board()

    #func to find all possible L shape moves
    def paths(src,board):
        #locate the index of the src  
        src_row = src // 8
        src_col = src % 8
        possible_moves = []
        #find possible L shapes
        if 0 <= src_row-2 < len(board):
            if 0 <= src_col -1 < 8:
                possible_moves.append(board[src_row-2][src_col -1])
                #count += 1
            if 0 <= src_col + 1 < 8:
                possible_moves.append(board[src_row-2][src_col + 1])
                #count += 1
        if 0 <= src_row+2 < len(board):
            if 0<= src_col -1 < 8:
                possible_moves.append(board[src_row+ 2][src_col -1])
                #count += 1
            if 0<= src_col +1 < 8:
                possible_moves.append(board[src_row+ 2][src_col +1])
                #count += 1
        if 0 <= src_row -1 < len(board):
            if 0<= src_col-2 < 8:
                possible_moves.append(board[src_row -1][src_col-2])
                #count += 1
            if 0<= src_col+2 < 8:
                possible_moves.append(board[src_row -1][src_col+2])
                #count += 1
        if 0 <= src_row +1 < len(board):
            if 0<= src_col-2 < 8:
                possible_moves.append(board[src_row +1][src_col-2])
                #count += 1
            if 0<= src_col+2 < 8:
                possible_moves.append(board[src_row +1][src_col+2])
                #count += 1
        
        return possible_moves
    
    def bfs(src, dest):
        q = deque() #Q to control moves and layers when moving in L shapes
        
        #base case
        if src == dest:
            return 0
        
        src_row = src // 8
        src_col = src % 8
        x = src_row
        y = src_col
        level = 0 #to control level
        q.append((x,y,level)) #0+> count
        visited =  {(x,y):1} #check if a coord is visited or not
        
        #do BFS
        while q:
            x,y,level = q.popleft()
            possible_paths = paths(x*8+y,board)
            for path in possible_paths:
                path_row = path // 8
                path_col = path % 8
                if path == dest:
                    return level+1
                if path not in visited:
                    visited[(path_row, path_col)] =1
                    q.append((path_row,path_col, level+1))
        
        return -1
    return bfs(src,dest)




print(solution(0,1))
    
