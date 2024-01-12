import tkinter as tk
from tkinter import messagebox


class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.current_player = "X"

        self.buttons = [[None, None, None] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(
                    root,
                    text="",
                    font=("normal", 20),
                    width=8,
                    height=4,
                    command=lambda i=i, j=j: self.on_button_click(i, j),
                )
                self.buttons[i][j].grid(row=i, column=j)

    def on_button_click(self, i, j):
        if self.buttons[i][j]["text"] == "" and not self.check_winner():
            self.buttons[i][j]["text"] = self.current_player
            if self.check_winner():
                messagebox.showinfo(
                    "Tic Tac Toe", f"Player {self.current_player} wins!"
                )
                self.reset_game()
            elif all(
                self.buttons[row][col]["text"] != ""
                for row in range(3)
                for col in range(3)
            ):
                messagebox.showinfo("Tic Tac Toe", "It's a draw!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        # Check rows, columns, and diagonals for a winner
        for i in range(3):
            if (
                self.buttons[i][0]["text"]
                == self.buttons[i][1]["text"]
                == self.buttons[i][2]["text"]
                != ""
            ):
                return True
            if (
                self.buttons[0][i]["text"]
                == self.buttons[1][i]["text"]
                == self.buttons[2][i]["text"]
                != ""
            ):
                return True
        if (
            self.buttons[0][0]["text"]
            == self.buttons[1][1]["text"]
            == self.buttons[2][2]["text"]
            != ""
        ):
            return True
        if (
            self.buttons[0][2]["text"]
            == self.buttons[1][1]["text"]
            == self.buttons[2][0]["text"]
            != ""
        ):
            return True
        return False

    def reset_game(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]["text"] = ""
        self.current_player = "X"


if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
