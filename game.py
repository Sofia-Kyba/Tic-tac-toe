""" Module for playing game"""
# all imports
from Tic_tac_toe.board import Board


def mainGame():
    """
    Function for simulating game.
    :return:
    """
    board = Board()
    print('Welcome to tic-tac-toe game!')
    print('Your initial board: ')
    print(board)
    while True:
        board.person_move()
        if board.check_win() is not None:
            if board.check_win() == 'X':
                print('You won!')
                return
            elif board.check_win() == '0':
                print('Computer won!')
                return
        board.computer_move()
        if board.check_win() == '0':
            print('Computer won!')
            return


if __name__ == '__main__':
    mainGame()
