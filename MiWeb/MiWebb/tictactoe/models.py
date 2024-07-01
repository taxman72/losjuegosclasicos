# models.py
from django.db import models

class TicTacToe(models.Model):
    board = models.CharField(max_length=9, default='         ')
    current_player = models.CharField(max_length=1, default='X')

    def make_move(self, position):
        if self.board[position] == ' ':
            self.board = f'{self.board[:position]}{self.current_player}{self.board[position + 1:]}'
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            self.save()

    def get_winner(self):
        for row in range(0, 9, 3):
            if self.board[row] == self.board[row + 1] == self.board[row + 2] != ' ':
                return self.board[row]
        for col in range(3):
            if self.board[col] == self.board[col + 3] == self.board[col + 6] != ' ':
                return self.board[col]
        if self.board[0] == self.board[4] == self.board[8] != ' ':
            return self.board[0]
        if self.board[2] == self.board[4] == self.board[6] != ' ':
            return self.board[2]
        return None

    def is_draw(self):
        return ' ' not in self.board and not self.get_winner()
