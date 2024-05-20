import random

class HumanPlayer:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(f"{self.letter}'s turno. Entre com uma posição (0-8): ")
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Posição inválida. Tente novamente.")
        return val

class RandomPlayer:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square

class UnbeatablePlayer:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        square = self.find_best_move(game)
        return square

    def find_best_move(self, game):
        opponent = 'O' if self.letter == 'X' else 'X'

        # 1. Ganhar se possível
        for square in game.available_moves():
            game.make_move(square, self.letter)
            if game.current_winner:
                game.board[square] = ' '
                game.current_winner = None
                return square
            game.board[square] = ' '

        # 2. Bloquear o oponente se ele estiver prestes a vencer
        for square in game.available_moves():
            game.make_move(square, opponent)
            if game.current_winner:
                game.board[square] = ' '
                game.current_winner = None
                return square
            game.board[square] = ' '

        # 3. Jogar no centro se disponível
        if 4 in game.available_moves():
            return 4

        # 4. Estratégia específica para evitar a armadilha das quinas opostas
        corners = [0, 2, 6, 8]
        opponent_moves = [i for i, spot in enumerate(game.board) if spot == opponent]

        if len(opponent_moves) == 1 and opponent_moves[0] in corners:
            corner_opposite = {0: 8, 2: 6, 6: 2, 8: 0}
            opposite_corner = corner_opposite[opponent_moves[0]]
            if opposite_corner in game.available_moves():
                return opposite_corner

        if len(opponent_moves) == 2:
            if set(opponent_moves) in [{0, 8}, {2, 6}]:
                sides = [1, 3, 5, 7]
                for side in sides:
                    if side in game.available_moves():
                        return side

        # 5. Jogar nos cantos se disponíveis
        for move in corners:
            if move in game.available_moves():
                return move

        # 6. Jogar nos lados se disponíveis
        for move in [1, 3, 5, 7]:
            if move in game.available_moves():
                return move

        # 7. Escolher aleatoriamente se nenhuma das opções acima estiver disponível
        return random.choice(game.available_moves())

