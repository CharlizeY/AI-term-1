from q7 import sudoku_board_valid

# the following board configurations are provided for testing purposes
# see boards.py if you want to look at them
from boards import (invalid_row_board, 
                   invalid_column_board,
                   invalid_box_board,
                   valid_incomplete_board,
                   valid_board1,
                   valid_board2,
                   valid_board3)

# print_board() prints out a visually appealing board
from boards import print_board


def test_valid_board1():
    print_board(valid_board1)
    result = sudoku_board_valid(valid_board1)
    assert result == True


def test_valid_board2():
    print_board(valid_board2)
    result = sudoku_board_valid(valid_board2)
    assert result == True


def test_valid_board3():
    print_board(valid_board3)
    result = sudoku_board_valid(valid_board3)
    assert result == True


def test_valid_board4():
    print_board(valid_incomplete_board)
    result = sudoku_board_valid(valid_incomplete_board)
    assert result == True


def test_invalid_rows():
    print_board(invalid_row_board)
    result = sudoku_board_valid(invalid_row_board)
    assert result == False


def test_invalid_cols():
    print_board(invalid_column_board)
    result = sudoku_board_valid(invalid_column_board)
    assert result == False


def test_invalid_boxes():
    print_board(invalid_box_board)
    result = sudoku_board_valid(invalid_box_board)
    assert result == False



if __name__ == "__main__":
    test_valid_board1()
    test_valid_board2()
    test_valid_board3()
    test_valid_board4()
    test_invalid_rows()
    test_invalid_cols()
    test_invalid_boxes()

