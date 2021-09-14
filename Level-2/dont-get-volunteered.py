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
    
    #find src and destination 
    
        
# level = 0
# count = 0
# if q.empty() == False:
#     src = q.get() #reset the src
#     count -= 1
#     if src == dest:
#         level += 1
#         return level
# level += 1
# paths(src,dest,board)





    



# solution(19,36) 
            #     while q.empty() == False:
            #         temp = q.get()
            #         if temp == dest:
            #             break
            #     level += 1
            # return level 

            #print(board[src_row +1][src_col+2])
            #from src, check 4 directions, see if L shape exist, if yes, work on the accordinly

            # number of the element in each level, level 1 =5elements , level 2 = 2 elements
            # queue = [1,2,3,4,5,7,8]
            # enque and count 
            # check each elements in the queue 
            #count = 0
            # (1),2,(3),4,5
            # 6.  7. 8. 9.10
            #[6,7,9,8] count =1
            # generate new moves from elem in the q
            # -> moves are updated with new L shapes
            # start to deq and count -- 
            #back to the loop, to enq the new moves
            # queue = [1,5] 
            # level+1 => deque base on count  => put possible move back to the queue, count +1
            
            
            #Spencer's 
            # (1),2,(3),4,5
            # 6.  7. 8. 9.10
            # [8]  
            #level + 1
            #[3,4]
            #
            # count = 1, level =1
        #     1   ---->0
        # 8       ---->1

            
            #once visited 1 layer, pop all elems of that layer out of Q --> 1 step has been done (num or step == num of layer visited)
            #while popping, check if des is in the elem, if yes, that layer is the answer. eg, des in layer 3 -> number of step is 3
            #if found des, break out of the loop. 0





    # while src >= 0 and dest <= 63:
    #     if src+1 == dest:
    #         return 3
    #     elif dest - src == 17 or dest - src == 15:
    #         return 1
    #     else:
#first, build the table
#then, find src and destination 
#do BFS from src
#have a Q to control steps and layers when moving, can find the number of steps accordingly.
#once visited 1 layer, pop all elems of that layer out of Q --> 1 step has been done (num or step == num of layer visited)
#while popping, check if des is in the elem, if yes, that layer is the answer. eg, des in layer 3 -> number of step is 3
#if found des, break out of the loop. 0


                # if 0 <= src_row-2 <= len(board):
                #     if 0 <= src_col -1 <= len(src_row-2):
                #         possible_moves.append(board[src_row-2][src_col -1])
                #     if 0 <= board[src_row-2][src_col + 1] <= len(board[src_row-2]):
                #         possible_moves.append(board[src_row-2][src_col + 1])
                # if 0 <= board[src_row+2] <= len(board):
                #     if 0<= board[src_row+ 2][src_col -1] <= len(board[src_row+2]):
                #         possible_moves.append(board[src_row+ 2][src_col -1])
                #     if 0<= board[src_row+ 2][src_col +1] <= len(board[src_row+2]):
                #         possible_moves.append(board[src_row+ 2][src_col +1])
                # if 0 <= board[src_row -1] <= len(board):
                #     if 0<= board[src_row -1][src_col-2] <= len(board[src_row -1]):
                #         possible_moves.append(board[src_row -1][src_col-2])
                #     if 0<= board[src_row -1][src_col+2] <= len(board[src_row -1]):
                #         possible_moves.append(board[src_row -1][src_col+2])
                # if 0 <= board[src_row +1] <= len(board):
                #     if 0<= board[src_row +1][src_col-2] <= len(board[src_row +1]):
                #         possible_moves.append(board[src_row +1][src_col-2])
                #     if 0<= board[src_row + 1][src_col+2] <= len(board[src_row +1]):
                #         possible_moves.append(board[src_row +1][src_col+2])




                # possible_moves = [board[src_row-2][src_col -1],
                #                 board[src_row-2][src_col + 1],
                #                 board[src_row+ 2][src_col -1],
                #                 board[src_row+2][src_col +1],
                #                 board[src_row -1][src_col-2],
                #                 board[src_row -1][src_col+2],
                #                 board[src_row +1][src_col-2],
                #                 board[src_row +1][src_col+2]]