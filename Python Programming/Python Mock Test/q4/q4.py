def get_winner(board):

    N = len(board)
    
    # Horizontal win
    for y in range(N):
        winner_marker = board[y][0]
        if (winner_marker != ' ') and \
            all([winner_marker == board[y][i] for i in range(1, N)]):
            print("Found horizontal win.")
            return winner_marker


    # Vertical win
    for x in range(N):
            winner_marker = board[0][x]
            if (winner_marker != ' ') and \
                all([winner_marker == board[i][x] for i in range(1, N)]):
                print("Found vertical win.")
                return winner_marker


    # Northwest diagonal win
    winner_marker = board[0][N-1]
    if (winner_marker != ' ') and \
        all([winner_marker == board[i][N-1-i] for i in range(1,N)]):
        print("Found north-west diag win.")
        return winner_marker


    # Northeast diagonal win
    winner_marker = board[0][0]
    if (winner_marker != ' ') and \
        all([winner_marker == board[i][i] for i in range(1,N)]):
        print("Found north-west win.")
        return winner_marker


    # Returns Draw iff there is no winner yet AND there are still empty cells 
    if any([board[y][x] == ' ' for x in range(N) for y in range(N)]):
        return None
    else:
        return "draw"

