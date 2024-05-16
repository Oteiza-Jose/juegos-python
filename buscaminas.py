import tkinter as tk
from tkinter import messagebox
from collections import deque
import random

class MinesweeperGUI:
    def __init__(self, master):
        # Inicializa la interfaz gráfica de Minesweeper
        self.master = master
        self.master.title("Minesweeper")
        self.generate_menu()
        self.level = None
        self.rows = None
        self.cols = None
        self.mines = None
        self.board = []
        self.buttons = []
        self.flags = []

    def generate_menu(self):
        # Genera el menú para seleccionar el nivel del juego
        menubar = tk.Menu(self.master)
        self.master.config(menu=menubar)
        level_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Level", menu=level_menu)
        level_menu.add_command(label="Basic", command=lambda: self.set_level("Basic"))
        level_menu.add_command(label="Intermediate", command=lambda: self.set_level("Intermediate"))
        level_menu.add_command(label="Advanced", command=lambda: self.set_level("Advanced"))

    def set_level(self, level):
        # Establece el nivel del juego y las dimensiones del tablero
        self.level = level
        if level == "Basic":
            self.rows, self.cols, self.mines = 3, 3, 3
        elif level == "Intermediate":
            self.rows, self.cols, self.mines = 6, 6, 6
        elif level == "Advanced":
            self.rows, self.cols, self.mines = 9, 9, 9
        self.generate_board()
        self.master.geometry(f"{self.cols * 30}x{self.rows * 30}")  # Ajustar tamaño de ventana al tablero

    def generate_board(self):
        # Genera el tablero del juego con celdas inicializadas en 0
        self.board = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        self.buttons = []
        self.flags = [[False for _ in range(self.cols)] for _ in range(self.rows)]
        self.place_mines()
        self.calculate_numbers()
        self.create_buttons()

    def place_mines(self):
        # Coloca las minas en el tablero de manera aleatoria
        self.mines_coordinates = []
        while len(self.mines_coordinates) < self.mines:
            row = random.randint(0, self.rows - 1)
            col = random.randint(0, self.cols - 1)
            if (row, col) not in self.mines_coordinates:
                self.mines_coordinates.append((row, col))

    def calculate_numbers(self):
        # Calcula los números para las celdas que no son minas
        for row, col in self.mines_coordinates:
            self.board[row][col] = -1  # Marcar la celda como una mina
            for i in range(-1, 2):
                for j in range(-1, 2):
                    new_row, new_col = row + i, col + j
                    if 0 <= new_row < self.rows and 0 <= new_col < self.cols:
                        if self.board[new_row][new_col] != -1:
                            self.board[new_row][new_col] += 1

    def create_buttons(self):
        # Crea los botones del tablero y les asigna eventos de clic
        for i in range(self.rows):
            row_buttons = []
            for j in range(self.cols):
                button = tk.Button(self.master, width=2, height=1, font=("Helvetica", 12, "italic"))
                button.grid(row=i, column=j)
                button.bind("<Button-1>", lambda event, row=i, col=j: self.reveal_cell(row, col))
                button.bind("<Button-3>", lambda event, row=i, col=j: self.toggle_flag(row, col))
                row_buttons.append(button)
            self.buttons.append(row_buttons)

    def reveal_cell(self, row, col):
        # Revela la celda seleccionada
        button = self.buttons[row][col]
        if button['state'] == tk.DISABLED or self.flags[row][col]:
            return

        if (row, col) in self.mines_coordinates:  # Verificar si la celda es una mina
            self.show_mines()  # Mostrar todas las minas
            messagebox.showinfo("Game Over", "Game Over! You hit a mine!")
            self.disable_all_buttons()  # Deshabilitar todos los botones
            return
        elif self.board[row][col] > 0:
            button.config(text=str(self.board[row][col]))
            button.config(state=tk.DISABLED)
        else:
            button.config(state=tk.DISABLED)
            visited = set()
            queue = deque([(row, col)])
            while queue:
                r, c = queue.popleft()
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        new_row, new_col = r + i, c + j
                        if 0 <= new_row < self.rows and 0 <= new_col < self.cols and (new_row, new_col) not in visited:
                            visited.add((new_row, new_col))
                            if self.board[new_row][new_col] >= 0:
                                self.buttons[new_row][new_col].config(state=tk.DISABLED)
                                if self.board[new_row][new_col] == 0:
                                    queue.append((new_row, new_col))
        if self.check_win():
            messagebox.showinfo("Congratulations", "You win!")

    def show_mines(self):
        # Muestra todas las minas en el tablero
        for row, col in self.mines_coordinates:
            button = self.buttons[row][col]
            if button:
                button.config(text='*')

    def disable_all_buttons(self):
        # Deshabilita todos los botones del tablero
        for row in self.buttons:
            for button in row:
                button.config(state=tk.DISABLED)

    def toggle_flag(self, row, col):
        # Marca o desmarca una celda con una bandera
        button = self.buttons[row][col]
        if button['state'] == tk.DISABLED:
            return
        if self.flags[row][col]:
            self.flags[row][col] = False
            button.config(text="")
        else:
            self.flags[row][col] = True
            button.config(text="🚩")

    def check_win(self):
        # Verifica si el jugador ha ganado el juego
        revealed_non_mine_cells = 0
        flagged_mines = 0
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] != -1 and self.buttons[i][j]['state'] == tk.DISABLED:
                    revealed_non_mine_cells += 1
                if self.board[i][j] == -1 and self.flags[i][j]:
                    flagged_mines += 1

        return revealed_non_mine_cells == (self.rows * self.cols - self.mines) and flagged_mines == self.mines

def main():
    # Función principal para iniciar el juego
    root = tk.Tk()
    game = MinesweeperGUI(root)
    root.title("Minesweeper")

    # Cambiar el icono de la ventana
    icon = tk.PhotoImage(file="images/mine.png")  # Reemplaza "path/to/your/icon.png" con la ruta de tu archivo de icono
    root.iconphoto(False, icon)

    root.mainloop()

if __name__ == "__main__":
    main()
