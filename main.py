from game import JogoDaVelha
from players import HumanPlayer, RandomPlayer, UnbeatablePlayer

def main():
    print("Bem-vindo ao Jogo da Velha!")
    print("Escolha o modo de jogo:")
    print("1. Usuário vs Aleatório")
    print("2. Usuário vs Não Perde")
    print("3. Aleatório vs Não Perde")

    choice = input("Digite o número do modo de jogo: ")

    if choice == '1':
        player1 = HumanPlayer("X")
        player2 = RandomPlayer("O")
        game = JogoDaVelha(player1, player2)
        game.play()

    elif choice == '2':
        player1 = HumanPlayer("X")
        player2 = UnbeatablePlayer("O")
        game = JogoDaVelha(player1, player2)
        game.play()

    elif choice == '3':
        num_games = int(input("Quantas partidas entre Aleatório e Não Perde? "))
        random_wins = 0
        unbeatable_wins = 0
        draws = 0

        for _ in range(num_games):
            player1 = RandomPlayer("X")
            player2 = UnbeatablePlayer("O")
            game = JogoDaVelha(player1, player2)
            result = game.play()
            if result == "X":
                random_wins += 1
            elif result == "O":
                unbeatable_wins += 1
            else:
                draws += 1

        print(f"Resultados após {num_games} partidas:")
        print(f"Aleatório venceu: {random_wins}")
        print(f"Não Perde venceu: {unbeatable_wins}")
        print(f"Empates: {draws}")

    else:
        print("Escolha inválida. Saindo do jogo.")

if __name__ == "__main__":
    main()