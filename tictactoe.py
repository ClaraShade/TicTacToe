from enum import Enum

class Result(Enum):
    win_x = 1
    win_o = 2
    not_finished = 3
    draw = 4

class Square:
    def __init__(self, num, col, row):
        self.num = num
        self.col = col
        self.row = row
        self.is_empty = True
        self.char = '_'

    def __repr__(self):
        return self.char

    def set_x(self):
        self.is_empty = False
        self.char = 'x'

    def set_o(self):
        self.is_empty = False
        self.char = 'o'

    def is_available(self):
        return self.is_empty

class Board:
    def __init__(self, side):
        self.length = side
        self.squares = []
        self.filled = 0
        self.full = False
        square_index = 1
        for column in range(1, self.length + 1):
            row_list = []
            for row in range(1, self.length + 1):
                new_square = Square(square_index, column, row)
                if square_index < self.length**2:
                    square_index = square_index + 1
                row_list.append(new_square)
            self.squares.append(row_list)

    def is_full(self):
        if self.filled == self.length**2:
            self.full = True

    def printme(self):
        rowcount = 0
        for i in self.squares:
            rowcount = rowcount + 1
            if rowcount < 10:
                print("Row "+str(rowcount)+" "+str(i))
            else:
                print("Row" + str(rowcount) + " " + str(i))
        columns = "Column:"
        for i in range(1, self.length+1):
            columns = columns+str(i)+", "
        print(columns)

    def mark_x(self, mark_row, mark_column):
        self.squares[mark_row][mark_column].set_x()
        self.filled = self.filled + 1

    def mark_o(self, mark_row, mark_column):
        self.squares[mark_row][mark_column].set_o()
        self.filled = self.filled + 1

    def check_rows(self): #czy da się zrobić niestatyczną funkcję #a może ify
        for i in range(self.length):
            counter = 0
            for j in range(self.length):
                mark = str(self.squares[i][j])
                if mark == 'x':
                    counter = counter + 1
                elif mark == 'o':
                    counter = counter - 1
                else:
                    pass
            if counter == int(self.length):
                return 1
            elif counter == int(self.length) * -1:
                return 2
            else:
                return 3

    def check_cols(self):
        for i in range(self.length):
            counter = 0
            for j in range(self.length):
                mark = str(self.squares[j][i])
                if mark == 'x':
                    counter = counter + 1
                elif mark == 'o':
                    counter = counter - 1
                else:
                    pass
            if counter == int(self.length):
                return 1
            elif counter == int(self.length) * -1:
                return 2
            else:
                return 3

    def check_diagonal_l(self):
        counter = 0
        for i in range(self.length):
            mark = str(self.squares[i][i])
            if mark == 'x':
                counter = counter + 1
            elif mark == 'o':
                counter = counter - 1
            else:
                pass
        if counter == int(self.length):
            return 1
        elif counter == int(self.length) * -1:
            return 2
        else:
            return 3

    def check_diagonal_r(self):
        counter = 0
        for i in range(self.length):
            mark = str(self.squares[i][i*-1-1])
            if mark == 'x':
                counter = counter + 1
            elif mark == 'o':
                counter = counter - 1
            else:
                pass
        if counter == int(self.length):
            return 1
        elif counter == int(self.length) * -1:
            return 2
        else:
            return 3

def win_check():
    result = new_board.check_rows()
    if result !=3:
        end_game()
    else:
        result = new_board.check_cols()
        if result !=3:
            end_game()
        else:
            result = new_board.check_diagonal_l()
            if result !=3:
                end_game()
            else:
                result = new_board.check_diagonal_r()
    return result


def end_game():
    print("Thank you! Your game has ended!")
    exit()


def play():
    outcome = win_check()
    while outcome == 3:
        print("Mark x in: ")
        mark_row = int(input("row: "))-1
        mark_column = int(input("column: "))-1

        while not new_board.squares[mark_row][mark_column].is_empty:
            print("This square is not empty! Chose another")
            print("Mark x in: ")
            mark_row = int(input("row: ")) - 1
            mark_column = int(input("column: ")) - 1

        new_board.mark_x(mark_row, mark_column)
        print("Thank you! See your board below: ")
        new_board.printme()

        outcome = win_check()

        if outcome == 3:
            print("Mark o in: ")
            mark_row = int(input("row: "))-1
            mark_column = int(input("column: "))-1

            while not new_board.squares[mark_row][mark_column].is_empty:
                print("This square is not empty! Chose another")
                print("Mark o in: ")
                mark_row = int(input("row: ")) - 1
                mark_column = int(input("column: ")) - 1

            new_board.mark_o(mark_row, mark_column)
            print("Thank you! See your board below: ")
            new_board.printme()
            outcome = win_check()
            if outcome == 2:
                end_game()
            else:
                pass


#def outcome():
#    result = win_check()
#    if result == Result.win_x:
#       print("Congratulations! The x-player won!")
#        end_game()
#    elif result == Result.win_o:
#        print("Congratulations! The o-player won!")
#        end_game()
#    elif result == Result.draw:
#        print("It's a draw!")
#        end_game()
#    else:
#        print("Next move!")

while True:
    try:
        side = int(input("How wide board you want to create? Please, type natural number greater than 1: "))
        while side < 2:
            print("You think you are a rebel, huh? Nice try!")
            side = int(input("Please, type natural number: "))
        break
    except ValueError:
        print("We are not great in math, are we? N-A-T-U-R-A-L number!")


new_board = Board(side)
print("Congratulations! You created " + str(side) + "-sided board, which has " + str(side**2) + " squares.")
print("See your board below:")
new_board.printme()

play()