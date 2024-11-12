import numpy
import pygame

from gameBoard import Board

class GamePlay:
    def __init__(self, board:Board):
        self.gridSize = 60
        self.edgeSize = 15

        self.scoreOfBlack = 0
        self.scoreOfWhite = 0
        self.isTurnOfBlack = True
        self.isGameOver = False
        self.winner = 0

        self.board = board
        self.startX = 40
        self.startY = 30
        self.lastMove = None


    def handlePlayer(self, event):
        originX = self.startX - self.edgeSize
        originY = self.startY - self.edgeSize

        size = (self.board.size - 1) * self.gridSize + self.edgeSize * 2
        position = event.pos

        if originX <= position[0] <= originX+size and originY <= position[1] <= originY+size:
            row = int((position[0]-originX)//self.gridSize)
            column = int ((position[1]-originY)//self.gridSize)
            self.setPiece(row, column)
            self.isTurnOfBlack = not self.isTurnOfBlack


    def setPiece(self,row,column):
        if self.board.matrix[row][column] == 0:
            self.board.matrix[row][column] = 2 if self.isTurnOfBlack else 1
            self.lastMove = (row, column)
            return True
        return False
        

