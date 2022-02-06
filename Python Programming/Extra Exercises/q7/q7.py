import itertools

def sudoku_board_valid(board):
    
    # Horizontal check
    list_of_rows = []
    
    for i in range(9):
        row = [board[i][j] for j in range(9)]
        new_row = [entry for entry in row if entry != '.']
        list_of_rows.append(new_row)
        are_valid_rows = all(len(row) == len(set(row)) for row in list_of_rows)

                  
    # Vertical check
    list_of_cols = []
    
    for j in range(9):
        col = [board[i][j] for i in range(9)]
        new_col = [entry for entry in col if entry != '.']
        list_of_cols.append(new_col)
        are_valid_cols = all(len(col) == len(set(col)) for col in list_of_cols)

             
    # Box check
    list_of_boxs = []
    
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            # Flatten the list of list using itertools
            box = list(itertools.chain.from_iterable(row[j:j+3] for row in board[i:i+3]))
            new_box = [entry for entry in box if entry != '.']
            list_of_boxs.append(new_box)
            are_valid_boxs = all(len(box) == len(set(box)) for box in list_of_boxs)


    # Check if the board satisfies all three conditions
    return all([are_valid_rows, are_valid_cols, are_valid_boxs]) 
        
