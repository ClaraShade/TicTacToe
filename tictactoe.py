class Board:
    def __init__(self, side):
        self.length = side
        self.squares = side**2
        self.picture = []
        self.filled = 0


class Square:
    def __init__(self, num, col, row):
        self.num = num
        self.col = col
        self.row = row
        self.is_empty = True
        self.char = '_'

    def __repr__(self):
        return self.char

    def mark_x(self):
        self.is_empty = False
        self.char = 'x'

    def mark_o(self):
        self.is_empty = False
        self.char = 'o'


def createboard():
    side = int(input("How wide board you want to create? Please, type natural number: "))
    new_board = Board(side)
    square_index = 1
    for column in range(1, new_board.length+1):
        row_list = []
        for row in range(1, new_board.length+1):
            new_square = Square(square_index, column, row)
            print(new_square.num, new_square.col, new_square.row, new_square)
            if square_index < new_board.squares:
                square_index = square_index+1
            row_list.append(new_square)
        new_board.picture.append(row_list)

    print("Congratulations! You created " + str(side) + "-sided board, which has " + str(square_index) + " squares.")
    print("See your board below:")
    return new_board


board = createboard()

for i in board.picture:
    print(i)


def to_mark_x():
    print("Mark x in: ")
    mark_row = int(input("row: "))-1
    mark_column = int(input("column: "))-1

    while not board.picture[mark_row][mark_column].is_empty:
        print("This square is not empty! Chose another")
        print("Mark x in: ")
        mark_row = int(input("row: ")) - 1
        mark_column = int(input("column: ")) - 1

    board.picture[mark_row][mark_column].mark_x()
    print("Thank you! See your board below: ")
    for i in board.picture:
        print(i)


def to_mark_o():
    print("Mark o in: ")
    mark_row = int(input("row: "))-1
    mark_column = int(input("column: "))-1

    while not board.picture[mark_row][mark_column].is_empty:
        print("This square is not empty! Chose another")
        print("Mark o in: ")
        mark_row = int(input("row: ")) - 1
        mark_column = int(input("column: ")) - 1

    board.picture[mark_row][mark_column].mark_o()
    print("Thank you! See your board below: ")
    for i in board.picture:
        print(i)


def start_game():
    print(board.squares)
    while board.filled < board.squares:
        to_mark_x()
        board.filled = board.filled + 1
        print(board.filled)
        if board.filled < board.squares:
            to_mark_o()
            board.filled = board.filled + 1
        else:
            break
    print("Thank you! Your game has ended!")


start_game()
