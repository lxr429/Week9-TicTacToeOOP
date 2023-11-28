import unittest
from logic import TicTacToe
from players import HumanPlayer, BotPlayer


class TestTicTacToe(unittest.TestCase):
    def test_initialization(self):
        game = TicTacToe()
        self.assertEqual(game.board, [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ])
        self.assertIsNone(game.winner)

    def test_player_assignment(self):
        game = TicTacToe()
        human_player = HumanPlayer('X')
        bot_player = BotPlayer('O')

        self.assertEqual(human_player.symbol, 'X')
        self.assertEqual(bot_player.symbol, 'O')

    def test_take_turn_human_player(self):
        game = TicTacToe()
        player = HumanPlayer('X')
        player_input = (1, 2)

        row, col = player.take_turn(game.board)

        self.assertEqual((row, col), player_input)

    def test_take_turn_bot_player(self):
        game = TicTacToe()
        player = BotPlayer('O')

        turn = player.take_turn(game.board)

        self.assertIn(turn, [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)])

    def test_player_switching(self):
        game = TicTacToe()
        player1 = HumanPlayer('X')
        player2 = BotPlayer('O')

        self.assertEqual(game.other_player(player1.symbol), 'O')
        self.assertEqual(game.other_player(player2.symbol), 'X')

    def test_valid_move(self):
        game = TicTacToe()
        player = HumanPlayer('X')
        row, col = (2, 2)

        valid = game.is_valid_move(row, col)

        self.assertTrue(valid)

    def test_invalid_move_occupied(self):
        game = TicTacToe()
        player = HumanPlayer('X')
        row, col = (2, 2)

        # Occupy a cell
        game.board[1][1] = 'O'

        valid = game.is_valid_move(row, col)

        self.assertFalse(valid)

    def test_invalid_move_out_of_bounds(self):
        game = TicTacToe()
        player = HumanPlayer('X')
        row, col = (4, 2)

        valid = game.is_valid_move(row, col)

        self.assertFalse(valid)

    def test_get_winner_row(self):
        game = TicTacToe()
        game.board = [
            ['X', 'X', 'X'],
            [None, None, None],
            [None, None, None],
        ]

        winner = game.get_winner()

        self.assertEqual(winner, 'X')

    def test_get_winner_column(self):
        game = TicTacToe()
        game.board = [
            ['O', None, None],
            ['O', None, None],
            ['O', None, None],
        ]

        winner = game.get_winner()

        self.assertEqual(winner, 'O')

    def test_get_winner_diagonal(self):
        game = TicTacToe()
        game.board = [
            ['O', None, None],
            [None, 'O', None],
            [None, None, 'O'],
        ]

        winner = game.get_winner()

        self.assertEqual(winner, 'O')

    def test_get_winner_draw(self):
        game = TicTacToe()
        game.board = [
            ['X', 'O', 'X'],
            ['O', 'X', 'O'],
            ['O', 'X', 'O'],
        ]

        winner = game.get_winner()

        self.assertEqual(winner, 'Draw')


if __name__ == '__main__':
    unittest.main()
