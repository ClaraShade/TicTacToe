#!/usr/bin/env python3

from enum import Enum


class Result(Enum):
    win_x = 1
    win_o = 2
    not_finished = 3
    draw = 4


class Square:
    def __init__(self, number, column, row):
        self.number = number
        self.column = column
        self.row = row
        self.is_empty = True
        self.character = '_'

    def __repr__(self):
        return self.character

    def set_x(self):
        self.is_empty = False
        self.character = 'x'

    def set_o(self):
        self.is_empty = False
        self.character = 'o'


class Board:
    def __init__(self, side):
        self.length = side
        self.squares = []
        self.filled = 0
        self.full = False
        self.state = Result.not_finished
        square_index = 1
        for column in range(1, self.length + 1):
            row_list = []
            for row in range(1, self.length + 1):
                new_square = Square(square_index, column, row)
                if square_index < self.length**2:
                    square_index = square_index + 1
                row_list.append(new_square)
            self.squares.append(row_list)

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

    def check_rows(self):
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
                self.state = Result.win_x
                return self.state
            elif counter == int(self.length) * -1:
                self.state = Result.win_o
                return self.state
            else:
                if self.full:
                    self.state = Result.draw
                    return self.state
                else:
                    self.state = Result.not_finished

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
                self.state = Result.win_x
                return self.state
            elif counter == int(self.length) * -1:
                self.state = Result.win_o
                return self.state
            else:
                if self.full:
                    self.state = Result.draw
                    return self.state
                else:
                    self.state = Result.not_finished

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
            self.state = Result.win_x
            return self.state
        elif counter == int(self.length) * -1:
            self.state = Result.win_o
            return self.state
        else:
            if self.full:
                self.state = Result.draw
                return self.state
            else:
                self.state = Result.not_finished

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
            self.state = Result.win_x
            return self.state
        elif counter == int(self.length) * -1:
            self.state = Result.win_o
            return self.state
        else:
            if self.full:
                self.state = Result.draw
                return self.state
            else:
                self.state = Result.not_finished

    def win_check(self):
        self.check_rows()
        if self.state != Result.not_finished:
            pass
        else:
            self.check_cols()
            if self.state != Result.not_finished:
                pass
            else:
                self.check_diagonal_l()
                if self.state != Result.not_finished:
                    pass
                else:
                    self.check_diagonal_r()
                    if self.state == Result.not_finished:
                        if self.filled == self.length ** 2:
                            self.state = Result.draw
                        else:
                            pass


def create_game():
    while True:
        try:
            side = int(input("How wide board you want to create? Please, type natural number greater than 1: "))
            while side < 2:
                print("We are not great in math, are we? N-A-T-U-R-A-L number!")
                side = int(input("Please, type natural number greater than 1: "))
            break
        except ValueError:
            print("You think you are a rebel, huh? Nice try!")

    new_board = Board(side)
    print("Congratulations! You created " + str(side) + "-sided board, which has " + str(side**2) + " squares.")
    print("See your board below:")
    new_board.printme()
    return new_board


def outcome(board):
    board.win_check()
    if board.state == Result.win_x:
        print("Congratulations! The x-player won!")
        end_game()
    elif board.state == Result.win_o:
        print("Congratulations! The o-player won!")
        end_game()
    elif board.state == Result.draw:
        print("It's a draw!")
        end_game()
    else:
        print("Next move!")


def end_game():
    print("Thank you! Your game has ended!")
    just_waiting_input = input()
    exit()


def play(anyboard):
    while anyboard.state == Result.not_finished:
        print("Mark x in: ")
        mark_row = int(input("row: "))-1
        while not mark_row in range (0,anyboard.length):
            print("Please type a number between 1 and "+str(anyboard.length))
            mark_row = int(input("row: ")) - 1

        mark_column = int(input("column: "))-1
        while not mark_column in range(0, anyboard.length):
            print("Please type a number between 1 and " + str(anyboard.length))
            mark_column = int(input("row: ")) - 1

        while not anyboard.squares[mark_row][mark_column].is_empty:
            print("This square is not empty! Chose another")
            print("Mark x in: ")
            mark_row = int(input("row: ")) - 1
            mark_column = int(input("column: ")) - 1

        anyboard.mark_x(mark_row, mark_column)
        print("Thank you! See your board below: ")
        anyboard.printme()
        outcome(anyboard)

        if anyboard.state == Result.not_finished:
            print("Mark o in: ")
            mark_row = int(input("row: "))-1
            mark_column = int(input("column: "))-1

            while not anyboard.squares[mark_row][mark_column].is_empty:
                print("This square is not empty! Chose another")
                print("Mark o in: ")
                mark_row = int(input("row: ")) - 1
                mark_column = int(input("column: ")) - 1

            anyboard.mark_o(mark_row, mark_column)
            print("Thank you! See your board below: ")
            anyboard.printme()
            outcome(anyboard)
            if anyboard.state != Result.not_finished:
                end_game()
            else:
                pass

def main():
    new_board = create_game()
    play(new_board)

if __name__ == '__main__':
    main()