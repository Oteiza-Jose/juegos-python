import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Cruz y Círculo")
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'
        self.buttons = []
        self.create_buttons()
        self.create_reset_button()

    def create_buttons(self):
        for i in range(9):
            button = tk.Button(self.master, text=' ', font=('Arial', 20), width=5, height=2,
                               command=lambda i=i: self.player_move(i))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)

    def create_reset_button(self):
        reset_button = tk.Button(self.master, text='Reset', font=('Arial', 15), command=self.reset_game)
        reset_button.grid(row=3, column=0, columnspan=3, sticky='nsew')

    def player_move(self, index):
        if self.board[index] == ' ' and self.current_player == 'X':
            self.board[index] = 'X'
            self.buttons[index].config(text='X', state=tk.DISABLED)
            if self.check_winner('X'):
                messagebox.showinfo("Cruz y Círculo", "¡Has ganado!")
                self.disable_all_buttons()
            elif ' ' not in self.board:
                messagebox.showinfo("Cruz y Círculo", "¡Empate!")
                self.disable_all_buttons()
            else:
                self.current_player = 'O'
                self.master.after(500, self.machine_move)  # Añadir retraso de 500 ms

    def machine_move(self):
        empty_indices = [i for i, spot in enumerate(self.board) if spot == ' ']
        if empty_indices:  # Verificar que haya movimientos posibles
            index = random.choice(empty_indices)
            self.board[index] = 'O'
            self.buttons[index].config(text='O', state=tk.DISABLED)
            if self.check_winner('O'):
                messagebox.showinfo("Cruz y Círculo", "¡La máquina ha ganado!")
                self.disable_all_buttons()
            elif ' ' not in self.board:
                messagebox.showinfo("Cruz y Círculo", "¡Empate!")
                self.disable_all_buttons()
            else:
                self.current_player = 'X'

    def check_winner(self, player):
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8], # Horizontal
            [0, 3, 6], [1, 4, 7], [2, 5, 8], # Vertical
            [0, 4, 8], [2, 4, 6]             # Diagonal
        ]
        for condition in win_conditions:
            if all(self.board[i] == player for i in condition):
                return True
        return False

    def disable_all_buttons(self):
        for button in self.buttons:
            button.config(state=tk.DISABLED)

    def reset_game(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'
        for button in self.buttons:
            button.config(text=' ', state=tk.NORMAL)

def main():
    root = tk.Tk()
    game = TicTacToe(root)
    icon = tk.PhotoImage(file="images/circuloycruz.png")
    root.iconphoto(False, icon)
    root.mainloop()

if __name__ == "__main__":
    main()
