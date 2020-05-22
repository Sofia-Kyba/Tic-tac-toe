""" Module for creating board for the game """
# all imports
import random
import copy
from btree import BinaryTree


class Board:
    """ Class for representation board """

    def __init__(self):
        """ Create new board """
        self.last_move = ''
        self._field = [['-', '-', '-'],
                       ['-', '-', '-'],
                       ['-', '-', '-']]

    def possible(self):
        """
        Define possible positions
        :return: list
        """
        freePositions = []
        for i in range(len(self._field)):
            for j in range(len(self._field[i])):
                if self._field[i][j] == '-':
                    freePositions.append((i, j))
        return freePositions

    def person_move(self):
        """
        Simulate person's action. Person chooses position.
        Value at this position becomes 'X'.
        :return: NoneType
        """
        possiblePositions = self.possible()
        print('Possible positions: {}'.format(possiblePositions))
        chosenRow = int(input('Choose a row: '))
        chosenCol = int(input('Choose a col: '))
        choice = (chosenRow, chosenCol)
        if choice not in possiblePositions:
            chosenRow = int(input('Choose another row: '))
            chosenCol = int(input('Choose another col: '))
        self.add_pos(chosenRow, chosenCol, 'X')
        self.last_move = 'X'
        print(self)

    def computer_move(self):
        """
        Opportunity for computer to make move.
        :return:
        """
        self._field = self.tree_creation()._field
        print(self)

    def tree_creation(self):
        """
        Create new tree.
        :return:
        """
        tree = BinaryTree(self._field)

        def recursive(board, tree, move=None):
            possible = board.possible()

            if len(possible) == 1:
                pass
            else:
                new_move1 = random.choice(possible)
                possible.remove(new_move1)
                new_move2 = random.choice(possible)
                possible.remove(new_move2)

                board1 = copy.deepcopy(board)
                board2 = copy.deepcopy(board)

                next_move = ''
                if self.last_move == 'X':
                    self.last_move = '0'
                    next_move = '0'
                elif self.last_move == '0':
                    self.last_move = 'X'
                    next_move = 'X'

                board1.add_pos(new_move1[0], new_move1[1], next_move)
                board2.add_pos(new_move2[0], new_move2[1], next_move)
                tree.insertLeft(board1)
                tree.insertRight(board2)

                recursive(board1, tree.getLeft(), next_move)
                recursive(board2, tree.getRight(), next_move)

        recursive(self, tree)

        if self.win(tree.getAllLeaves()) >\
                self.win(tree.getAllLeaves()):
            return tree.left.key
        else:
            return tree.right.key

    def add_pos(self, row, col, value):
        """
        Add value to the needed position
        :return:
        """
        self._field[row][col] = value

    def win(self, leaves):
        """
        Check each leaf, that represents board.
        :return:
        """
        result = 0
        for leaf in leaves:
            winner = leaf.win_combination()
            if winner == 'X':
                result += -1
            else:
                result += 1
        return result

    def win_combination(self):
        """
        Return number of winning combinations.
        :return:
        """
        # check whether there are 3 'X' or 3 '0' in raw.
        for row in self._field:
            if row == ['X', 'X', 'X']:
                winner = 'X'
                return winner
            elif row == ['0', '0', '0']:
                winner = '0'
                return winner

        # check whether there are 3 'X' or 3 '0' in diagonal
        if self._field[0][0] == self._field[1][1] == \
                self._field[2][2] == 'X' or \
                self._field[0][2] == self._field[1][1] == \
                self._field[2][0] == 'X':
            winner = 'X'
            return winner
        elif self._field[0][0] == self._field[1][1] == \
                self._field[2][2] == '0' or \
                self._field[0][2] == self._field[1][1] == \
                self._field[2][0] == '0':
            winner = '0'
            return winner

        # check whether there are 3 'X' or 3 '0' in one column
        for i in range(3):
            if self._field[0][i] == self._field[1][i] == \
                    self._field[2][i] == 'X':
                winner = 'X'
                return winner
            elif self._field[0][i] == self._field[1][i] == \
                    self._field[2][i] == '0':
                winner = '0'
                return winner

        return None

    def check_win(self):
        """
        Check winner
        :return:
        """
        if not self.win_combination():
            return None
        elif self.win_combination() == 'X':
            flag = 'X'
        else:
            flag = '0'
        return flag

    def __str__(self):
        """
        Return string representation of board.
        :return:
        """
        line = ''
        for row in self._field:
            for column in row:
                line += str(column)
                line += ' '
            line += '\n'
        return line
