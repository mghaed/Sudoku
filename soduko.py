board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]
print(board)



def valid(bo, num, pos):
    #seach if the num exist in the row
    for i in range(len(bo)):
        if bo[pos[0]][i] == num and pos[1]!=i: #indx not equal to the inx of num that we already added
            return False
    
    
    #seach if the num exist in the column
    for i in range(len(bo[0])):
        if bo[i][pos[1]] == num and pos[0]!=i:
            return False
  
        
    #search in 3*3 square box
    box_x = pos[0] // 3
    box_y = pos[1] // 3
    
    for i in range(box_x*3 , box_y*3 + 3):
        for j in range(box_y*3 , box_x*3 + 3):
            if bo[i][j] == num and  (i,j) != pos:
                return False
    return True
                
        







# display board in 3*3 cubes
def print_board(bo):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("-----------------------")
            
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print (' | ', end='') 
            if j == 8:
                print(board[i][j])
            else:
                print(board[i][j], end=' ')   
                
      
            
 #find empty elements
def find_empty(bo): #Input board/ output position of emty value
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i,j) # (posision) indx of 0
                            #pos[0]=row
                            #pos[1]=column


