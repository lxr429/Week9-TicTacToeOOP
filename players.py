# players.py
import random


class HumanPlayer:
    def __init__(self, symbol):
        self.symbol = symbol

    def take_turn(self, board):
        row, col = map(int, input(f"Enter row and column for {self.symbol} (e.g., 1 2): ").split())
        return row, col


class BotPlayer:
    def __init__(self, symbol):
        self.symbol = symbol

    def take_turn(self, board):
        available_positions = [(i+1, j+1) for i in range(3) for j in range(3) if board[i][j] is None]
        return random.choice(available_positions) if available_positions else None