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

    # def checkRow(self, color):
    #     neg_color = 1 if color == 2 else 2
    #     for i in range(self.size):
    #         for j in range(self.size-4):
    #             window = self.matrix[i, j:j+5]
    #             if numpy.equal(window, numpy.ones(5) * color).all():
    #                 if 0 <= j-1 and j+5 < self.size:
    #                     if self.matrix[i, j-1] == neg_color and self.matrix[i, j+5] == neg_color:
    #                         continue
    #                 return True
    #     return False
    
    # def checkCol(self, color):
    #     neg_color = 1 if color == 2 else 2
    #     for i in range(self.size-4):
    #         for j in range(self.size):
    #             window = self.matrix[i:i+5, j]
    #             if numpy.equal(window, numpy.ones(5) * color).all():
    #                 if 0 <= i-1 and i+5 < self.size:
    #                     if self.matrix[i-1, j] == neg_color and self.matrix[i+5, j] == neg_color:
    #                         continue
    #                 return True
    #     return False

    # def checkDiagonal(self, color):
    #     neg_color = 1 if color == 2 else 2
    #     for i in range(self.size-4):
    #         for j in range(self.size-4):
    #             window = self.matrix[i:i+5, j:j+5]
    #             if numpy.equal(window.diagonal(), numpy.ones(5) * color).all():
    #                 if 0 <= i-1 and i+5 < self.size and 0 < j-1 and j+5 < self.size:
    #                     if self.matrix[i-1, j-1] == neg_color and self.matrix[i+5, j+5] == neg_color:
    #                         continue
    #                 return True
    #             if numpy.equal(numpy.fliplr(window).diagonal(), numpy.ones(5) * color).all():
    #                 if 0 <= i-1 and i+5 < self.size and 0 < j-1 and j+5 < self.size:
    #                     if self.matrix[i-1, j+5] == neg_color and self.matrix[i+5, j-1] == neg_color:
    #                         continue
    #                 return True
    #     return False

    # def checkWin(self, color):
    #     if self.checkRow(color):
    #         return True
    #     if self.checkCol(color):
    #         return True
    #     if self.checkDiagonal(color):
    #         return True
    #     return False

    
    def generateMoves(self):
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

