import numpy
import pygame
import time
import math


class Board:
    def __init__(self, board=None, matrix=None, size=None):
        if board is not None:
            self.matrix = numpy.array(board.matrix)
        if matrix is not None:
            self.matrix = numpy.array(matrix)
        if size is not None:
            self.matrix = numpy.zeros((size,size))
        self.size = self.matrix.shape[0]

    
    
    def generateMoves(self): #only adjacent
        moves = []
        for i in range(self.size):
            for j in range(self.size):
                if self.matrix[i, j] > 0:
                    continue
                if i > 0: # above row
                    if j > 0: # Top-left
                        if self.matrix[i-1][j-1] > 0 or self.matrix[i][j-1] > 0:
                            moves.append((i, j))
                            continue
                    if j < self.size - 1: # Top-right
                        if self.matrix[i-1][j+1] > 0 or self.matrix[i][j+1] > 0:
                            moves.append((i, j))
                            continue
                    if self.matrix[i-1][j] > 0: # Top
                        moves.append((i, j))
                        continue
                if i < self.size - 1: # below row
                    if j > 0: # Bottom-left
                        if self.matrix[i+1][j-1] > 0 or self.matrix[i][j-1] > 0:
                            moves.append((i, j))
                            continue
                    if j < self.size - 1: # Bottom-right
                        if self.matrix[i+1][j+1] > 0 or self.matrix[i][j+1] > 0:
                            moves.append((i, j))
                            continue
                    if self.matrix[i+1][j] > 0: # Bottom
                        moves.append((i, j))
                        continue
        return moves


    def draw(self, move, is_black):
        color = 2 if is_black else 1
        self.matrix[move] = color

    def swap(self):
        board = Board(matrix=self.matrix)
        for i in range(board.size):
            for j in range(board.size):
                if board.matrix[i][j] == 1:
                    board.matrix[i][j] = 2
                elif board.matrix[i][j] == 2:
                    board.matrix[i][j] = 1
        return board

