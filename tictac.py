import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")

        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]

        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.root, text="", font=('Helvetica', 20), width=6, height=3,
                                                command=lambda i=i, j=j: self.make_move(i, j))
                self.buttons[i][j].grid(row=i, column=j)

        self.root.mainloop()

    def make_move(self, i, j):
        if self.board[i][j] == "":
            self.board[i][j] = self.current_player
            self.buttons[i][j].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
                self.root.quit()
            elif self.check_draw():
                messagebox.showinfo("Tic Tac Toe", "It's a draw!")
                self.root.quit()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True
        return False

    def check_draw(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "":
                    return False
        return True

if __name__ == "__main__":
    game = TicTacToe()
