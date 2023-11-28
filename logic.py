# logic.py

import csv
import os

class TicTacToe:
    LOG_FILE = 'logs/game_log.csv'

    def __init__(self, player1_type, player2_type):
        self.board = self.make_empty_board()
        self.winner = None
        self.player1_type = player1_type
        self.player2_type = player2_type

    @staticmethod
    def make_empty_board():
        return [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]

    def get_winner(self):
        for n in range(3):
            if self.board[n][0] == self.board[n][1] == self.board[n][2] and self.board[n][0] is not None:
                return self.board[n][0]
            if self.board[0][n] == self.board[1][n] == self.board[2][n] and self.board[0][n] is not None:
                return self.board[0][n]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] is not None:
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] is not None:
            return self.board[0][2]
        if all(self.board[i][j] is not None for i in range(3) for j in range(3)):
            return 'Draw'

    def other_player(self, player):
        return 'O' if player == 'X' else 'X'

    def print_board(self):
        for row in self.board:
            print(" | ".join(cell if cell is not None else " " for cell in row))
            print("-" * 9)

    def is_valid_move(self, row, col):
        if row is None or col is None:
            return False
        if 1 <= row <= 3 and 1 <= col <= 3:
            if self.board[row - 1][col - 1] is None:
                return True
        return False
    
    def record_winner(self, winner):
        with open(self.LOG_FILE, mode='a', newline='') as file:
            writer = csv.writer(file)
            # Check if the file is empty and write the header row if it is
            if file.tell() == 0:
                writer.writerow(['Winner', 'Player1', 'Player2', 'MoveCount'])
            writer.writerow([winner, 'X' if self.player1_type == 'human' else 'Bot',
                             'O' if self.player2_type == 'human' else 'Bot', sum(1 for row in self.board for cell in row if cell)])
