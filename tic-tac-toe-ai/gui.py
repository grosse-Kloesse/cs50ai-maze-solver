import tkinter as tk
from tictactoe import *
from main import *

class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe - Play vs AI")
        self.board = initial_state()
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.label = None
        self.create_board()
        self.create_reset_button()

    def create_board(self):
        for i in range(3):
            for j in range(3):
                btn = tk.Button(self.root, text="", font=('Arial', 40), width=5, height=2,
                                command=lambda i=i, j=j: self.make_move(i, j))
                btn.grid(row=i, column=j)
                self.buttons[i][j] = btn

    def create_reset_button(self):
        reset_btn = tk.Button(self.root, text="Reset", font=('Arial', 14),
                              command=self.reset_game)
        reset_btn.grid(row=4, column=0, columnspan=3, pady=10)

    def make_move(self, i, j):
        if self.board[i][j] is None and not terminal(self.board):
            self.board[i][j] = player(self.board)
            self.update_buttons()

            if terminal(self.board):
                self.end_game()
                return

            # AI move
            ai_move = minimax(self.board)
            if ai_move:
                ai_i, ai_j = ai_move
                self.board[ai_i][ai_j] = player(self.board)
                self.update_buttons()

                if terminal(self.board):
                    self.end_game()

    def update_buttons(self):
        for i in range(3):
            for j in range(3):
                val = self.board[i][j]
                self.buttons[i][j]['text'] = val if val else ""

    def end_game(self):
        win = winner(self.board)
        msg = f"Winner: {win}" if win else "Draw!"
        for row in self.buttons:
            for btn in row:
                btn.config(state="disabled")
        self.label = tk.Label(self.root, text=msg, font=('Arial', 20))
        self.label.grid(row=3, column=0, columnspan=3)

    def reset_game(self):
        self.board = initial_state()
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="", state="normal")
        if self.label:
            self.label.destroy()
            self.label = None

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToeGUI(root)
    root.mainloop()