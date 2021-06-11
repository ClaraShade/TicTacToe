class Board:
    def __init__(self, x):
        self.length = x
        self.squares = x**2

class Square:
    def __init__(self, num, col, row):
        self.num = num
        self.col = col
        self.row = row
        self.is_empty = True

    def mark(self, char):
        self.is_empty = False
        self.char = 'cross'

def createboard():
    new_board = Board(3)
    square_index = 1
    for column in range (1,new_board.length+1):
        for row in range(1, new_board.length+1):
            new_square = Square(square_index, column, row)
            square_index = square_index+1
            print(new_square.num, new_square.col, new_square.row)
    return new_board

board = createboard()

print(board.length)
print(board.squares)