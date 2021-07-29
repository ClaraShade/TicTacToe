class Board:
    def __init__(self, side):
        self.length = side
        self.squares = side**2
        self.picture = []


class Square:
    def __init__(self, num, col, row):
        self.num = num
        self.col = col
        self.row = row
        self.is_empty = True
        self.char = ' '

    def mark_x(self):
        self.is_empty = False
        self.char = 'x'

    def mark_o(self):
        self.is_empty = False
        self.char = 'o'


def createboard():
    side = int(input("How wide board you want to create? Please, type natural number: "))
    new_board = Board(side)
    row_list = []
    square_index = 1
    for column in range(1, new_board.length+1):
        row_list.append(" ")
        for row in range(1, new_board.length+1):
            new_square = Square(square_index, column, row)
            print(new_square.num, new_square.col, new_square.row)
            if square_index < new_board.squares:
                square_index = square_index+1
        new_board.picture.append(row_list)
    print("Congratulations! You created " + str(side) + "-sided board, which has " + str(square_index) + " squares.")
    print("See your board below:")
    for i in new_board.picture:
        print(i)


board = createboard()
