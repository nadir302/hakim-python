class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # A list to hold 9 spaces
        self.current_winner = None  # Keep track of the winner

    def print_board(self):
        # Display current board
        print()
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]}")
        print("-----------")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]}")
        print("-----------")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]}")
        print()

    @staticmethod
    def print_board_positions():
        # Show guide for positions
        print("\nBoard Positions:")
        print(" 1 | 2 | 3")
        print("-----------")
        print(" 4 | 5 | 6")
        print("-----------")
        print(" 7 | 8 | 9\n")

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # Check row
        row_index = square // 3
        row = self.board[row_index*3 : (row_index+1)*3]
        if all([spot == letter for spot in row]):
            return True

        # Check column
        col_index = square % 3
        column = [self.board[col_index + i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        # Check diagonals
        if square % 2 == 0:
            diag1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diag1]):
                return True
            diag2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diag2]):
                return True

        return False


def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_positions()

    letter = 'X'  # Starting player

    while game.empty_squares():
        if letter == 'O':
            square = get_player_move(o_player, game)
        else:
            square = get_player_move(x_player, game)

        if game.make_move(square, letter):
            if print_game:
                print(f"\n{letter} makes a move to square {square + 1}")
                game.print_board()

            if game.current_winner:
                if print_game:
                    print(f"🎉 Player {game.current_winner} wins!")
                return game.current_winner

            # Switch player
            letter = 'O' if letter == 'X' else 'X'

    if print_game:
        print("It's a tie!")

def get_player_move(player, game):
    valid_square = False
    val = None
    while not valid_square:
        try:
            square = int(input(f"Player '{player}' turn. Choose position (1-9): ")) - 1
            if square not in game.available_moves():
                raise ValueError("That square is already taken or invalid.")
            valid_square = True
            val = square
        except ValueError as e:
            print(e)
    return val

# 🎮 Main Game Loop
if __name__ == '__main__':
    print("🌟 Welcome to Tic Tac Toe 🌟")
    while True:
        tictactoe = TicTacToe()
        play(tictactoe, 'X', 'O')

        again = input("\nDo you want to play again? (y/n): ").lower()
        if again != 'y':
            print("Thanks for playing! Goodbye!")
            break