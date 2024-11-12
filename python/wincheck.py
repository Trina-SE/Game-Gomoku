import numpy


class WinCheck:
    def __init__(self, board):
        self.board = board

    def checkRow(self, color):
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

    def checkCol(self, color):
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

    def checkDiagonal(self, color):
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

    def checkWin(self, color):
        if self.checkRow(color):
            return True
        if self.checkCol(color):
            return True
        if self.checkDiagonal(color):
            return True
        return False