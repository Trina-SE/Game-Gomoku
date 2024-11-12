import numpy
import pygame
import time
import math

from gameBoard import Board
from wincheck import WinCheck
from gameEngine import GameEngine

class GamePlay:
    def __init__(self, board:Board):
        self.gridSize = 60
        self.edgeSize = self.gridSize // 4

        self.scoreOfBlack = 0
        self.scoreOfWhite = 0
        self.isTurnOfBlack = True
        self.isGameOver = False
        self.winner = 0

        self.board = board
        self.winChecker = WinCheck(board)
        self.startX, self.startY  = 40,30
        # self.startY = 30
        self.lastMove = None


    def handlePlayer(self, e):
        originX = self.startX - self.edgeSize
        originY = self.startY - self.edgeSize
        size = (self.board.size - 1) * self.gridSize + self.edgeSize * 2
        pos = e.pos
        if originX <= pos[0] <= originX + size and originY <= pos[1] <= originY + size:
            x = pos[0] - originX
            y = pos[1] - originY
            row = int(y // self.gridSize)
            col = int(x // self.gridSize)
            self.setPiece(row, col)
        self.isTurnOfBlack = not self.isTurnOfBlack

    
    def handleAI(self, player):
        isBlack = player == 2
        row, column = GameEngine.findNextMove(self.board, 3, isBlack)
        self.setPiece(row, column)
        self.isTurnOfBlack = not self.isTurnOfBlack


    def setPiece(self,row,column):
        if self.board.matrix[row][column] == 0:
            self.board.matrix[row][column] = 2 if self.isTurnOfBlack else 1
            self.lastMove = (row, column)
            return True
        return False

    def winningCheck(self):
        if self.winChecker.checkWin(1):
            self.winner = 1
            self.isGameOver = True
        if self.winChecker.checkWin(2):
            self.winner = 2
            self.isGameOver = True
        
    def drawBoard(self, screen):

        # BACKGROUND
        pygame.draw.rect(screen, (86, 101, 185), [self.startX - self.edgeSize, self.startY - self.edgeSize, (self.board.size - 1)* self.gridSize + self.edgeSize * 2, (self.board.size - 1) * self.gridSize + self.edgeSize * 2], 0)

        # VERTICAL LINES
        for r in range(self.board.size):
            y = self.startY + r * self.gridSize
            pygame.draw.line(screen, (255,255,255), [self.startX, y], [self.startX + self.gridSize * (self.board.size - 1), y], 2)
        
        # HORIZONTAL LINES
        for c in range(self.board.size):
            x = self.startX + c * self.gridSize
            pygame.draw.line(screen, (255,255,255), [x, self.startY], [
                             x, self.startY + self.gridSize * (self.board.size - 1)], 2)

        # PIECE
        for r in range(self.board.size):
            for c in range(self.board.size):
                piece = self.board.matrix[r][c]
                if piece != 0:
                    if piece == 1:
                        color = (255, 255, 255)
                    else:
                        color = (0, 0, 0)

                    x = self.startX + c * self.gridSize
                    y = self.startY + r * self.gridSize
                    pygame.draw.circle(screen, color, [x, y], self.gridSize // 2)
        

