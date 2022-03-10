#!/usr/bin/env python3

"""
TicTacToe
This is an "hot seat" Easy TicTacToe game, created as my first approach to the
object-oriented-programming. The game runs in command line and communicates with the users via
text interface. The game enables to choose the width of the board. The 'x' player starts.
"""
import sys
from enum import Enum


class Result(Enum):
    """The Result class uses enum module to define the four possible states of the game
    WIN_X: the 'x' player won
    WIN_O: the 'o' player won
    NOT_FINISHED: the game is not finished yet
    DRAW: it's a DRAW"""
    WIN_X = 1
    WIN_O = 2
    NOT_FINISHED = 3
    DRAW = 4


class Square:
    """The Square class defines the particular square of the gameboard. The squares start as empty
    square, which corresponds to the '_' character """
    def __init__(self, number, column, row):
        self.number = number
        self.column = column
        self.row = row
        self.is_empty = True
        self.character = '_'

    def __repr__(self):
        """the method defines the representation of the square while printed"""
        return self.character

    def set_x(self):
        """the method sets square's state as not empty and sets 'x' on the square"""
        self.is_empty = False
        self.character = 'x'

    def set_o(self):
        """the method sets square's state as not empty and sets 'o' on the square"""

        self.is_empty = False
        self.character = 'o'


class Board:
    """The Board class defines the gameboard and stores the state of the game. When initiated,
    the Squares are created within the Board. The number of filled squares is set to 0 and the state
    of the game is set to not finished """
    def __init__(self, side):
        self.length = side
        self.squares = []
        self.filled = 0
        self.full = False
        self.state = Result.NOT_FINISHED
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
        """the method prints the Board representation to the screen"""
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
        """Marks chosen square as 'x' by calling the Square's set_x method
        and increases the number of filled squares on the Board by 1"""
        self.squares[mark_row][mark_column].set_x()
        self.filled = self.filled + 1


    def mark_o(self, mark_row, mark_column):
        """Marks chosen square as 'o' by calling the Square's set_o method
        and increases the number of filled squares on the Board by 1"""
        self.squares[mark_row][mark_column].set_o()
        self.filled = self.filled + 1


    def check_rows(self):
        """Returns the current state of the game based on the number
        of 'x' and 'o' marks in each row"""
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
                self.state = Result.WIN_X
            elif counter == int(self.length) * -1:
                self.state = Result.WIN_O
            else:
                if self.full:
                    self.state = Result.DRAW
                else:
                    self.state = Result.NOT_FINISHED
            return self.state


    def check_cols(self):
        """Returns the current state of the game based on the number
        of 'x' and 'o' marks in each column"""
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
                self.state = Result.WIN_X
            elif counter == int(self.length) * -1:
                self.state = Result.WIN_O
            else:
                if self.full:
                    self.state = Result.DRAW
                else:
                    self.state = Result.NOT_FINISHED
            return self.state


    def check_diagonal_l(self):
        """Returns the current state of the game based on the number of 'x'
        and 'o' marks in the first diagonal (upper left to bottom right)"""
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
            self.state = Result.WIN_X
        elif counter == int(self.length) * -1:
            self.state = Result.WIN_O
        else:
            if self.full:
                self.state = Result.DRAW
            else:
                self.state = Result.NOT_FINISHED
        return self.state


    def check_diagonal_r(self):
        """Returns the current state of the game based on the number of 'x'
        and 'o' marks in the second diagonal (upper right to bottom left)"""
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
            self.state = Result.WIN_X
        elif counter == int(self.length) * -1:
            self.state = Result.WIN_O
        else:
            if self.full:
                self.state = Result.DRAW
            else:
                self.state = Result.NOT_FINISHED
        return self.state


    def win_check(self):
        """Sequentially calls the four abovementioned methods to return the
        current state of the game. At the end, if the game state is
        NOT_FINISHED and the board is full, the state is changed to DRAW"""
        self.check_rows()
        if self.state != Result.NOT_FINISHED:
            pass
        else:
            self.check_cols()
            if self.state != Result.NOT_FINISHED:
                pass
            else:
                self.check_diagonal_l()
                if self.state != Result.NOT_FINISHED:
                    pass
                else:
                    self.check_diagonal_r()
                    if self.state == Result.NOT_FINISHED:
                        if self.filled == self.length ** 2:
                            self.state = Result.DRAW
                        else:
                            pass


def create_game():
    """Communicates with the user to create the game. Creates the Board based on
    the user input, prints and returns the new_board variable"""
    while True:
        try:
            side = int(input("How wide board you want to create?"
                             "Please, type natural number greater than 1: "))
            while side < 2:
                print("We are not great in math, are we? N-A-T-U-R-A-L number!")
                side = int(input("Please, type natural number greater than 1: "))
            break
        except ValueError:
            print("You think you are a rebel, huh? Nice try!")

    new_board = Board(side)
    print("Congratulations! You created " + str(side) + "-sided board, which has "
          + str(side**2) + " squares.")
    print("See your board below:")
    new_board.printme()
    return new_board


def outcome(board):
    """Prints the current state of the game to the console"""
    board.win_check()
    if board.state == Result.WIN_X:
        print("Congratulations! The x-player won!")
        end_game()
    elif board.state == Result.WIN_O:
        print("Congratulations! The o-player won!")
        end_game()
    elif board.state == Result.DRAW:
        print("It's a DRAW!")
        end_game()
    else:
        print("Next move!")


def end_game():
    """Prints the ending message to the console"""
    print("Thank you! Your game has ended!")
    input()
    sys.exit()


def play(anyboard):
    """Actual gameplay - untill the state of the game is equal to NOT_FINISHED,
    it sequentially asks the user to choose the square to mark 'x' and 'o'
    characters, checking if the square isn't already taken """
    while anyboard.state == Result.NOT_FINISHED:
        print("Mark x in: ")
        mark_row = int(input("row: "))-1
        while mark_row not in range(0, anyboard.length):
            print("Please type a number between 1 and "+str(anyboard.length))
            mark_row = int(input("row: ")) - 1

        mark_column = int(input("column: "))-1
        while mark_column not in range(0, anyboard.length):
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

        if anyboard.state == Result.NOT_FINISHED:
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
            if anyboard.state != Result.NOT_FINISHED:
                end_game()
            else:
                pass


def main():
    """Main game function - creates and plays the game"""
    new_board = create_game()
    play(new_board)


if __name__ == '__main__':
    main()
