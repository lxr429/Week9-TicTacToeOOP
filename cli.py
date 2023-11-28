# cli.py
import logging
from logic import TicTacToe
from players import HumanPlayer, BotPlayer

logging.basicConfig(
    filename='logs/game.log',  # Specify the log file location
    level=logging.INFO,         # Set the log level (INFO, DEBUG, WARNING, ERROR, etc.)
    format='%(asctime)s - %(levelname)s - %(message)s'
)

if __name__ == '__main__':
    logging.info("Game started.")

    player1_type = input("Select player 1 type (human/bot): ").lower()
    logging.info(f"player X is {player1_type}")
    player2_type = input("Select player 2 type (human/bot): ").lower()
    logging.info(f"player O is {player2_type}")
    
    game = TicTacToe(player1_type, player2_type)

    if player1_type == 'human':
        player1 = HumanPlayer('X')
    else:
        player1 = BotPlayer('X')

    if player2_type == 'human':
        player2 = HumanPlayer('O')
    else:
        player2 = BotPlayer('O')

    current_player = player1.symbol

    while game.winner is None:
        game.print_board()

        if game.other_player(current_player) == 'O':
            row, col = player1.take_turn(game.board)
        else:
            row, col = player2.take_turn(game.board)

        if not game.is_valid_move(row, col):
            logging.warning("Invalid input from the player.")
            continue

        game.board[row - 1][col - 1] = current_player
        logging.info(f"Player {current_player} placed {current_player} at ({row}, {col}).")

        game.winner = game.get_winner()

        if game.winner == 'Draw':
            game.print_board()
            print("It's a draw!")
            logging.info("The game ended in a draw.")
            game.record_winner('Draw')
            break
        elif game.winner:
            game.print_board()
            print(f"Player {game.winner} wins!")
            logging.info(f"Player {game.winner} wins the game.")
            game.record_winner(game.winner)
            break

        current_player = game.other_player(current_player)

    game.print_board()
    logging.info("Game ended.")