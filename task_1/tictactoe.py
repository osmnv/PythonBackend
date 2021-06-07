
''' TicTacToe Game '''

class TicTacToe:
    ''' TicTacToe Game '''

    SEPARATOR  = "   ------------"
    PLAYERS    = ("X", "O")

    def __init__(self):
        self._board = [['-', '-', '-'],
                       ['-', '-', '-'],
                       ['-', '-', '-']]
        self._step_counter = 0

    def print_board(self):
        '''Print the board'''

        print("     1   2   3")
        print(type(self).SEPARATOR)
        for i in range(3):
            print(" {} | {} | {} | {} |".format(i+1, *self._board[i]))
            print(type(self).SEPARATOR)

    def _check_pos(self, inp):
        '''Check if position is valid'''

        if not (inp.isdigit()
                and len(inp) == 2
                and int(inp[0]) in range(1, 4)
                and int(inp[1]) in range(1, 4)
                and self._board[int(inp[0]) - 1][int(inp[1]) - 1]) == '-':
            return "INVALID"
        return "OK"

    def _check_win(self):
        '''Check if game is over'''

        ptrn = "Player {} won!"

        for i in range(3):
            # Checking rows
            if [self._board[i][0]] * 3 == self._board[i] != ['-'] * 3:
                return ptrn.format(self._board[i][0])
            # Checking columns
            if ([self._board[j][i] for j in range(3)] == [self._board[0][i]] * 3
                                                      != ['-'] * 3):
                return ptrn.format(self._board[0][i])

        # Checking the main diagonal
        if ([self._board[i][i] for i in range(3)] == [self._board[0][0]] * 3
                                                  != ['-'] * 3):
            return ptrn.format(self._board[0][0])

        # Checking the side diagonal
        if ([self._board[1 + i][1 - i] for i in range(-1, 2)]
             == [self._board[0][2]] * 3
             != ['-'] * 3):
            return ptrn.format(self._board[0][2])

        # Checking whether it's draw
        if self._step_counter == 9:
            return "Draw!"

        return None


    def start_game(self):
        ''' Start the game '''

        self.print_board()
        while True:
            for player in TicTacToe.PLAYERS:
                print("Enter {} position: ".format(player))
                pos = input()
                while self._check_pos(pos) == "INVALID":
                    print("Position is not valid, try again: ")
                    pos = input()
                self._board[int(pos[0]) - 1][int(pos[1]) - 1] = player
                self._step_counter += 1
                self.print_board()
                if (res := self._check_win()) is not None:
                    print(res)
                    return

if __name__ == '__main__':
    game = TicTacToe()
    game.start_game()
