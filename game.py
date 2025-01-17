class JogoDaVelha:
    def __init__(self, player1, player2):
        self.board = [" " for _ in range(9)]
        self.current_winner = None
        self.player1 = player1
        self.player2 = player2

    def print_board(self):
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            print("| " + " | ".join(row) + " |")

    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        for row in number_board:
            print("| " + " | ".join(row) + " |")

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == " "]

    def empty_squares(self):
        return " " in self.board

    def num_empty_squares(self):
        return self.board.count(" ")

    def make_move(self, square, letter):
        if self.board[square] == " ":
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        row_ind = square // 3
        row = self.board[row_ind * 3:(row_ind + 1) * 3]
        if all([s == letter for s in row]):
            return True

        col_ind = square % 3
        column = [self.board[col_ind + i * 3] for i in range(3)]
        if all([s == letter for s in column]):
            return True

        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([s == letter for s in diagonal2]):
                return True

        return False

    def play(self):
        self.print_board_nums()
        letter = "X"

        while self.empty_squares():
            if letter == "O":
                square = self.player2.get_move(self)
            else:
                square = self.player1.get_move(self)

            if self.make_move(square, letter):
                print(f"{letter} faz um movimento para a posição {square}")
                self.print_board()
                print("")

                if self.current_winner:
                    print(f"{letter} vence!")
                    return letter

                letter = "O" if letter == "X" else "X"

        print("É um empate!")
        return "D"
