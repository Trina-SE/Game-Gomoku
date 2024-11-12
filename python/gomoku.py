import numpy
import pygame
import time
import math

from gamePlay import GamePlay
from gameEngine import GameEngine
from gameBoard import Board
from player import Player

PVP = "PlayerVsPlayer"
PVA = "PlayerVsAI"
AVA = "AIVsAI"


class GoMokuUI():
    
    def __init__(self, size:int, mode="PlayerVsAI"):
        pygame.init()
        pygame.display.set_caption("GOMOKU")

        self.width = 60 * size + 30
        self.height = 60 * size + 30 + 150
        self.screen = pygame.display.set_mode((60 * size + 30, 60 * size + 30 + 150))
        self.mode = mode
        self.going = True
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("arial", 24)

        board = Board(size=size)
        self.game = GamePlay(board)

    
    def loop(self):
        while self.going:
            self.update()
            self.draw()
            self.clock.tick(60)

        pygame.quit()


    def handlePlayerEvent(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                self.going = False
            elif e.type == pygame.MOUSEBUTTONDOWN:
                self.game.handlePlayer(e)
    

    def update(self):
        self.game.winningCheck()
        if self.game.isGameOver:
            return

        if self.mode == PVA:
            if self.game.isTurnOfBlack:
                self.handlePlayerEvent()
            else:
                self.handlePlayerEvent()
                self.game.handleAI(Player.WHITE)

        elif self.mode == PVP:
            self.handlePlayerEvent()

        elif self.mode == AVA:
            self.handlePlayerEvent()
            if self.game.isTurnOfBlack:
                self.game.handleAI(Player.BLACK)
            else:
                self.game.handleAI(Player.WHITE)
        self.game.black_score = GameEngine.getScore(self.game.board, True, not self.game.isTurnOfBlack)
        self.game.white_score = GameEngine.getScore(self.game.board, False, not self.game.isTurnOfBlack)

    def draw(self):
        self.screen.fill((255, 255, 255))
        # self.screen.blit(self.font.render("FPS: {0:.2F}".format(self.clock.get_fps()), True, (0, 0, 0)), (10, 10))
        # self.screen.blit(self.font.render("Black: {0}".format(self.game.scoreOfBlack), True, (0, 0, 0)), (10, self.height - 25))
        # self.screen.blit(self.font.render("White: {0}".format(self.game.white_score), True, (0, 0, 0)), (10, self.height - 50))
        # self.screen.blit(self.font.render("Calculation time: {0:0.2f}s".format(GameEngine.calculationTime), True, (0, 0, 0)), (10, self.height - 75))
        # self.screen.blit(self.font.render("Number of calculations: {0}".format(GameEngine.countEvaluation), True, (0, 0, 0)), (10, self.height - 100))
        self.screen.blit(self.font.render("Turn: {0}".format("Black" if self.game.isTurnOfBlack else "White"), True, (0, 0, 0)), (10, self.height - 125))

        self.game.drawBoard(self.screen)
        if self.game.isGameOver:
            self.screen.blit(self.font.render("{0} Win".format("Black" if self.game.winner == 2 else "White"), True, (0, 0, 0)), (self.width // 4 * 3, 10))

        pygame.display.update()    