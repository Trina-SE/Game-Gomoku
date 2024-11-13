# Game-Gomoku

# Team: AI-dle

<b>Game description:</b><br>
Gomoku, also known as "five in a row", is a board game similar to tic-tac-toe but on a
larger board. It is a two-player, fully observable, deterministic, zero-sum game. Players take
turn in placing ‘stone’s in the board until one player can connect five stones of the same
color in a row horizontally, vertically or diagonally. It is typically played in a 15 X 15 board,
but for this project a 10 X 10 board is sufficient. Detailed information about the game can
be found in: https://en.wikipedia.org/wiki/Gomoku

# Gomoku

Clone repository

`git clone https://github.com/Trina-SE/Game-Gomoku`

### Installation Steps

1. Open a terminal or command prompt.
2. Navigate to the `python` directory of the project:
   ```bash
   cd python
   pip install pygame
   pip install numpy
   python main.py
   ```


Game options in main.py

`game = GomokuUI("Gomoku", 10, GomokuUI.PVP)` Player vs Player.

`game = GomokuUI("Gomoku", 10, GomokuUI.PVA)` Player vs AI.

`game = GomokuUI("Gomoku", 10, GomokuUI.AVA)` AI vs AI.
