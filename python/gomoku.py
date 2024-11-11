import numpy
import pygame


class WinCheck:
    def __init__(self, board):
        self.board = board

    def __check_row(self, color):
        neg_color = 1 if color == 2 else 2
        for i in range(self.board.size):
            for j in range(self.board.size - 4):
                window = self.board.matrix[i, j:j+5]
                if numpy.equal(window, numpy.ones(5) * color).all():
                    if 0 <= j - 1 and j + 5 < self.board.size:
                        if self.board.matrix[i, j - 1] == neg_color and self.board.matrix[i, j + 5] == neg_color:
                            continue
                    return True
        return False

    def __check_col(self, color):
        neg_color = 1 if color == 2 else 2
        for i in range(self.board.size - 4):
            for j in range(self.board.size):
                window = self.board.matrix[i:i+5, j]
                if numpy.equal(window, numpy.ones(5) * color).all():
                    if 0 <= i - 1 and i + 5 < self.board.size:
                        if self.board.matrix[i - 1, j] == neg_color and self.board.matrix[i + 5, j] == neg_color:
                            continue
                    return True
        return False

    def __check_diagonal(self, color):
        neg_color = 1 if color == 2 else 2
        for i in range(self.board.size - 4):
            for j in range(self.board.size - 4):
                window = self.board.matrix[i:i+5, j:j+5]
                if numpy.equal(window.diagonal(), numpy.ones(5) * color).all():
                    if 0 <= i - 1 and i + 5 < self.board.size and 0 <= j - 1 and j + 5 < self.board.size:
                        if self.board.matrix[i - 1, j - 1] == neg_color and self.board.matrix[i + 5, j + 5] == neg_color:
                            continue
                    return True
                if numpy.equal(numpy.fliplr(window).diagonal(), numpy.ones(5) * color).all():
                    if 0 <= i - 1 and i + 5 < self.board.size and 0 <= j - 1 and j + 5 < self.board.size:
                        if self.board.matrix[i - 1, j + 5] == neg_color and self.board.matrix[i + 5, j - 1] == neg_color:
                            continue
                    return True
        return False

    def check_win(self, color):
        if self.__check_row(color):
            return True
        if self.__check_col(color):
            return True
        if self.__check_diagonal(color):
            return True
        return False

class Board:
    def __init__(self, board=None, matrix=None, size=None):
        if board is not None:
            self.matrix = numpy.array(board.matrix)
        if matrix is not None:
            self.matrix = numpy.array(matrix)
        if size is not None:
            self.matrix = numpy.zeros((size,size))
        self.size = self.matrix.shape[0]

    # def __check_row(self, color):
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
    
    # def __check_col(self, color):
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

    # def __check_diagonal(self, color):
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

    # def check_win(self, color):
    #     if self.__check_row(color):
    #         return True
    #     if self.__check_col(color):
    #         return True
    #     if self.__check_diagonal(color):
    #         return True
    #     return False

    
    

