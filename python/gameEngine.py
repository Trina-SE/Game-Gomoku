import time
import math

from gameBoard import Board
from wincheck import WinCheck

class GameEngine:
    calculationTime = 0
    countEvaluation = 0

    @classmethod
    def getPatterns(cls, line, patternDict, isBlack):
        color = 2 if isBlack else 1
        negColor = 1 if isBlack else 2
        s = ''
        old = 0

        for i, c in enumerate(line):
            if i == 0:
                s += 'O'
            if c == color:
                if old == negColor:
                    s += 'O'
                s += 'X'
            if c != color or i == len(line)-1:
                if c == negColor and len(s) > 0:
                    s += 'O'
                elif i == len(line)-1:
                    s += 'O'
                if s in patternDict.keys():
                    patternDict[s] += 1
                else:
                    patternDict[s] = 1
                s = ''
            old = c

    @classmethod
    def getPatternsRow(cls, board: Board, patternDict, isBlack):
        size = board.size
        matrix = board.matrix
        for i in range(size):
            cls.getPatterns(matrix[i], patternDict, isBlack)

    @classmethod
    def getPatternsCol(cls, board: Board, patternDict, isBlack):
        size = board.size
        matrix = board.matrix
        for i in range(size):
            cls.getPatterns(matrix[:, i], patternDict, isBlack)

    @classmethod
    def getPatternsDiagonal(cls, board: Board, patternDict, isBlack):
        size = board.size
        matrix1 = board.matrix
        matrix2 = matrix1[::-1, :]
        for i in range(-size+1, size):
            cls.getPatterns(matrix1.diagonal(i), patternDict, isBlack)
            cls.getPatterns(matrix2.diagonal(i), patternDict, isBlack)

    @classmethod
    def evaluateBoard(cls, board: Board, isBlackTurn: bool):
        cls.countEvaluation += 1
        blackScore = cls.getScore(board, True, isBlackTurn)
        whiteScore = cls.getScore(board, False, isBlackTurn)
        if blackScore == 0: blackScore = 1.0
        return whiteScore / blackScore
    
    @classmethod
    def getScore(cls, board: Board, isBlack: bool, isBlackTurn: bool):
        patternDict = {}
        cls.getPatternsRow(board, patternDict, isBlack)
        cls.getPatternsCol(board, patternDict, isBlack)
        cls.getPatternsDiagonal(board, patternDict, isBlack)
        return cls.getConsecutiveScore(patternDict)

    @classmethod
    def getConsecutiveScore(cls, patternDict):
        score = 0
        for pattern in patternDict:
            if pattern.count('X') == 5:
                if pattern[0] == 'O' and pattern[-1] == 'O':
                    pass
                else:
                    score += 100000
            if pattern.count('X') == 4:
                if pattern[0] == 'O' and pattern[-1] == 'O':
                    pass
                elif pattern[0] == 'O' or pattern[-1] == 'O':
                    score += 5000 * patternDict[pattern]
                else:
                    score += 10000 * patternDict[pattern]
            if pattern.count('X') == 3:
                if pattern[0] == 'O' and pattern[-1] == 'O':
                    pass
                elif pattern[0] == 'O' or pattern[-1] == 'O':
                    score += 500 * patternDict[pattern]
                else:
                    score += 1000 * patternDict[pattern]
            if pattern.count('X') == 2:
                if pattern[0] == 'O' and pattern[-1] == 'O':
                    pass
                elif pattern[0] == 'O' or pattern[-1] == 'O':
                    score += 50 * patternDict[pattern]
                else:
                    score += 100 * patternDict[pattern]
            if pattern.count('X') == 1:
                if pattern[0] == 'O' and pattern[-1] == 'O':
                    pass
                else:
                    score += 1 * patternDict[pattern]
        return score

    @classmethod
    def findNextMove(cls, board: Board, depth, isBlack):
        cls.countEvaluation = 0
        cls.calculationTime = 0
        if isBlack:
            board = board.swap()

        start = time.time()
        value, bestMove = cls.searchWinningMove(board)
        if bestMove is not None:
            move = bestMove
        else:
            value, bestMove = cls.minimax_alphabeta(board, depth, -1.0, 100000000, True)
            if bestMove is None:
                move = None
            else:
                move = bestMove
        end = time.time()
        cls.calculationTime = end-start
        if move is None:
            move = (board.size//2, board.size//2)
        return move

    @classmethod
    def heuristic_sort(cls, board, allMoves):
        def customFunc(board, move):
            x, y = move
            count = 0
            size = board.size
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    if 0 <= x+i < size and 0 <= y+j < size:
                        if board.matrix[x+i][y+j] != 0:
                            count += 1
            return count

        return sorted(allMoves, key=lambda move: customFunc(board, move), reverse=True)

    @classmethod
    def minimax_alphabeta(cls, board: Board, depth, alpha, beta, isMax):
        if depth == 0:
            return (cls.evaluateBoard(board, not isMax), None)

        allPossibleMoves = board.generateMoves()
        allPossibleMoves = cls.heuristic_sort(board, allPossibleMoves)

        if len(allPossibleMoves) == 0:
            return (cls.evaluateBoard(board, not isMax), None)

        bestMove = None

        if isMax:
            bestValue = -math.inf
            for move in allPossibleMoves:
                tempBoard = Board(board=board)
                tempBoard.draw(move, False)
                value, tempMove = cls.minimax_alphabeta(tempBoard, depth-1, alpha, beta, not isMax)
                
                if value > alpha:
                    alpha = value
                if value >= beta:
                    return (value, tempMove)
                if value > bestValue:
                    bestValue = value
                    bestMove = move
        else:
            bestValue = math.inf
            for move in allPossibleMoves:
                tempBoard = Board(board=board)
                tempBoard.draw(move, True)
                value, tempMove = cls.minimax_alphabeta(tempBoard, depth-1, alpha, beta, not isMax)
                if value < beta:
                    beta = value
                if value <= alpha:
                    return (value, tempMove)
                if value < bestValue:
                    bestValue = value
                    bestMove = move
        return (bestValue, bestMove)

    @classmethod
    def searchWinningMove(cls, board: Board):
        allPossibleMoves = board.generateMoves()

        for move in allPossibleMoves:
            tempBoard = Board(board=board)
            tempBoard.draw(move, False)
            winCheck = WinCheck(tempBoard)
            if winCheck.checkWin(1):
                return (None, move)
            tempBoard = Board(board=board)
            tempBoard.draw(move, True)
            if winCheck.checkWin(2):
                return (None, move)
        return (None, None)