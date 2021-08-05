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

board.picture[0][1].mark_x()


#print(board.picture[0][0].col)

print("Mark x in: ")
mark_row = int(input("row: "))-1
mark_column = int(input("column: "))-1
#print(mark_row)
#print(mark_column)

while board.picture[mark_row][mark_column].is_empty != True:
    print("This square is not empty! Chose another")
    print("Mark x in: ")
    mark_row = int(input("row: ")) - 1
    mark_column = int(input("column: ")) - 1
    #print(mark_row)
    #print(mark_column)

board.picture[mark_row][mark_column].mark_x()
print(board.picture)